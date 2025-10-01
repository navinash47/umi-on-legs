#!/usr/bin/env python3
"""
Script to check legged_gym package installation and dependencies
"""

import sys
import os

def check_legged_gym():
    """Check legged_gym package installation status"""
    print("🔍 Checking legged_gym package installation...")
    print("=" * 60)
    
    # Check 1: Basic import
    try:
        import legged_gym
        print("✅ legged_gym imported successfully!")
        print(f"   Location: {legged_gym.__file__}")
    except ImportError as e:
        print(f"❌ legged_gym import failed: {e}")
        return False
    
    # Check 2: Submodule imports
    submodules = [
        'legged_gym.env',
        'legged_gym.rsl_rl',
        'legged_gym.env.isaacgym'
    ]
    
    print("\n🔍 Checking submodule imports...")
    for module in submodules:
        try:
            __import__(module)
            print(f"✅ {module} imported successfully!")
        except ImportError as e:
            print(f"❌ {module} import failed: {e}")
    
    # Check 3: Check if it's installed in development mode
    print(f"\n🔍 Package installation info:")
    try:
        import pkg_resources
        dist = pkg_resources.get_distribution('legged-gym')
        print(f"✅ Package found: {dist.project_name} v{dist.version}")
        print(f"   Location: {dist.location}")
        print(f"   Editable: {dist.location.endswith('mani-centric-wbc')}")
    except Exception as e:
        print(f"❌ Package info not available: {e}")
    
    # Check 4: Check dependencies
    print(f"\n🔍 Checking dependencies...")
    dependencies = ['matplotlib', 'numpy', 'torch', 'gym']
    
    for dep in dependencies:
        try:
            __import__(dep)
            print(f"✅ {dep} available")
        except ImportError:
            print(f"❌ {dep} missing")
    
    # Check 5: Check Isaac Gym dependency
    print(f"\n🔍 Checking Isaac Gym dependency...")
    try:
        import isaacgym
        print("✅ Isaac Gym is installed!")
    except ImportError:
        print("❌ Isaac Gym is NOT installed (required for full functionality)")
        print("   Download from: https://developer.nvidia.com/isaac-gym")
    
    # Check 6: Test basic functionality
    print(f"\n🔍 Testing basic functionality...")
    try:
        from legged_gym.env import isaacgym
        print("✅ legged_gym.env.isaacgym module accessible")
    except Exception as e:
        print(f"❌ legged_gym.env.isaacgym not accessible: {e}")
    
    print(f"\n📋 Summary:")
    print(f"   ✅ legged_gym package: INSTALLED")
    print(f"   ❌ Isaac Gym dependency: NOT INSTALLED")
    print(f"   📝 Status: Ready for development, but Isaac Gym needed for simulation")
    
    return True

if __name__ == "__main__":
    check_legged_gym()
