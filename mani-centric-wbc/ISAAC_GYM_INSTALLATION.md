# Isaac Gym Installation Guide

## Problem
The original error occurs because `isaacgym` is not available through pip. Isaac Gym must be downloaded and installed manually from NVIDIA's developer portal.

## Solution Steps

### 1. Download Isaac Gym
1. Go to [NVIDIA Isaac Gym Developer Portal](https://developer.nvidia.com/isaac-gym)
2. Sign up/log in with your NVIDIA account
3. Download **Isaac Gym Preview 4** (the latest version)
4. Extract the downloaded file to a location like `/home/anandyala/IsaacGym_Preview_4_Package`

### 2. Install Isaac Gym
After downloading and extracting Isaac Gym, run the following commands:

```bash
# Navigate to the extracted Isaac Gym directory
cd /path/to/IsaacGym_Preview_4_Package

# Install Isaac Gym in the conda environment
/home/anandyala/miniconda3/envs/isaac/bin/python setup.py install
```

### 3. Alternative: Manual Installation
If the above doesn't work, you can manually add Isaac Gym to your Python path:

```bash
# Add Isaac Gym to your environment
export PYTHONPATH="${PYTHONPATH}:/path/to/IsaacGym_Preview_4_Package/python"
```

### 4. Verify Installation
Test that Isaac Gym is properly installed:

```bash
# Activate the conda environment
source /home/anandyala/miniconda3/bin/activate isaac

# Test Isaac Gym import
python -c "import isaacgym; print('Isaac Gym installed successfully!')"
```

### 5. Install the legged_gym package
Once Isaac Gym is installed, you can install the legged_gym package:

```bash
cd /home/anandyala/acads/602/Project/umi-on-legs/mani-centric-wbc
pip install -e .
```

## Troubleshooting

### Common Issues:

1. **Library path issues**: If you get errors like `ImportError: libpython3.8.so.1.0: cannot open shared object file`, add the conda environment's library path:
   ```bash
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/anandyala/miniconda3/envs/isaac/lib/
   ```

2. **CUDA compatibility**: Ensure your CUDA version is compatible with Isaac Gym Preview 4.

3. **Graphics drivers**: Make sure you have proper NVIDIA graphics drivers installed.

## Next Steps
After successful installation, you can:
- Download the required data and checkpoints as described in the main README
- Run the training and evaluation scripts
- Use the visualization tools

## Notes
- Isaac Gym Preview 4 is the latest version and is compatible with this codebase
- The installation process may take some time due to the large size of Isaac Gym
- Make sure you have sufficient disk space (several GB) for the installation
