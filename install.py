import launch

if not launch.is_installed("scikit-learn"):
    launch.run_pip("install scikit-learn", "scikit-learn")

if not launch.is_installed("diffusers"):
    launch.run_pip("install diffusers", "diffusers")
