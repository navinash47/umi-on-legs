#!/bin/bash
# Isaac Gym Environment Activation Script
# This script sets up the environment for Isaac Gym and legged_gym

echo "🚀 Activating Isaac Gym environment..."

# Activate conda environment
source /home/anandyala/miniconda3/bin/activate isaac

# Set library path for Isaac Gym
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/anandyala/miniconda3/envs/isaac/lib/

# Navigate to project directory
cd /home/anandyala/acads/602/Project/umi-on-legs/mani-centric-wbc

echo "✅ Environment activated!"
echo "📁 Working directory: $(pwd)"
echo "🐍 Python: $(which python)"
echo "📦 Isaac Gym: $(python -c 'import isaacgym; print("✅ Available")' 2>/dev/null || echo "❌ Not available")"
echo "🤖 legged_gym: $(python -c 'import legged_gym; print("✅ Available")' 2>/dev/null || echo "❌ Not available")"

echo ""
echo "🎯 Ready to use Isaac Gym and legged_gym!"
echo "💡 Tip: Always run this script before using the project:"
echo "   source activate_environment.sh"
