import argparse, json, sys
from pathlib import Path
from src.utils import git_sha, mean_std, utc_now_iso

def run_episodes(policy_path, episodes, seed):
    import gymnasium as gym
    from stable_baselines3 import PPO
    env = gym.make("CartPole-v1")
    model = PPO.load(policy_path)
    rewards = []
    for ep in range(episodes):
        obs, _ = env.reset(seed=seed + ep)
        done, total = False, 0.0
        while not done:
            action, _ = model.predict(obs, deterministic=True)
            obs, reward, terminated, truncated, _ = env.step(action)
            total += float(reward)
            done = terminated or truncated
        rewards.append(total)
    return rewards

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--policy", type=Path, default=Path("out/policy.zip"))
    p.add_argument("--episodes", type=int, default=20)
    p.add_argument("--min-reward", type=float, default=450.0)
    p.add_argument("--seed", type=int, default=1234)
    p.add_argument("--out", type=Path, default=Path("out"))
    args = p.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    rewards = run_episodes(args.policy, args.episodes, args.seed)
    mean, std = mean_std(rewards)
    passed = mean >= args.min_reward
    metrics = {"mean_reward": round(mean, 2), "std_reward": round(std, 2),
               "episodes": args.episodes, "eval_seed": args.seed,
               "min_reward": args.min_reward, "gate_passed": passed,
               "git_sha": git_sha(), "evaluated_at": utc_now_iso()}
    meta = args.out / "train_meta.json"
    if meta.exists():
        metrics.update(json.loads(meta.read_text()))
    (args.out / "metrics.json").write_text(json.dumps(metrics, indent=2))
    print(f"Gate {'PASSED' if passed else 'FAILED'}: mean={mean:.1f} "
          f"std={std:.1f} (threshold {args.min_reward})")
    sys.exit(0 if passed else 1)

if __name__ == "__main__":
    main()
