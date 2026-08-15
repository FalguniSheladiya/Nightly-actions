import argparse, json, time
from pathlib import Path
from src.utils import git_sha, utc_now_iso

def main():
    import gymnasium as gym
    from stable_baselines3 import PPO
    p = argparse.ArgumentParser()
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--steps", type=int, default=40_000)
    p.add_argument("--out", type=Path, default=Path("out"))
    args = p.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    model = PPO("MlpPolicy", gym.make("CartPole-v1"), seed=args.seed, verbose=1)
    t0 = time.time()
    model.learn(total_timesteps=args.steps)
    model.save(args.out / "policy.zip")
    meta = {"seed": args.seed, "train_steps": args.steps,
            "train_duration_s": round(time.time() - t0, 1),
            "git_sha": git_sha(), "trained_at": utc_now_iso()}
    (args.out / "train_meta.json").write_text(json.dumps(meta, indent=2))

if __name__ == "__main__":
    main()
