#!/usr/bin/env python3
"""
Script to check Isaac Gym installation status
"""

import sys
import os

def check_isaac_gym():
    """Check if Isaac Gym is properly installed"""
    print("🔍 Checking Isaac Gym installation...")
    print("=" * 50)
    
    # Check 1: Try to import isaacgym
    try:
        import isaacgym
        print("✅ Isaac Gym import successful!")
        print(f"   Location: {isaacgym.__file__}")
        return True
    except ImportError as e:
        print(f"❌ Isaac Gym import failed: {e}")
    
    # Check 2: Look for Isaac Gym in common locations
    common_paths = [
        "/home/anandyala/IsaacGym_Preview_4_Package",
        "/home/anandyala/IsaacGym",
        "/home/anandyala/IsaacGym_Preview_3_Package",
        "/opt/IsaacGym",
        "/usr/local/IsaacGym"
    ]
    
    print("\n🔍 Checking common Isaac Gym locations...")
    found_paths = []
    for path in common_paths:
        if os.path.exists(path):
            print(f"✅ Found: {path}")
            found_paths.append(path)
        else:
            print(f"❌ Not found: {path}")
    
    if found_paths:
        print(f"\n💡 Isaac Gym found but not in Python path!")
        print("   To install, run:")
        for path in found_paths:
            print(f"   cd {path}")
            print(f"   /home/anandyala/miniconda3/envs/isaac/bin/python setup.py install")
    
    # Check 3: Check PYTHONPATH
    print(f"\n🔍 Current PYTHONPATH: {os.environ.get('PYTHONPATH', 'Not set')}")
    
    # Check 4: Check if Isaac Gym is in site-packages
    import site
    site_packages = site.getsitepackages()
    print(f"\n🔍 Checking site-packages: {site_packages}")
    
    for sp in site_packages:
        isaac_path = os.path.join(sp, "isaacgym")
        if os.path.exists(isaac_path):
            print(f"✅ Found isaacgym in: {isaac_path}")
            return True
    
    print("\n❌ Isaac Gym is not installed!")
    print("\n📋 To install Isaac Gym:")
    print("1. Download from: https://developer.nvidia.com/isaac-gym")
    print("2. Extract to: /home/anandyala/IsaacGym_Preview_4_Package")
    print("3. Run: cd /home/anandyala/IsaacGym_Preview_4_Package")
    print("4. Run: /home/anandyala/miniconda3/envs/isaac/bin/python setup.py install")
    
    return False

if __name__ == "__main__":
    check_isaac_gym()
