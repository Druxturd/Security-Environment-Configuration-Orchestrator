from cx_Freeze import Executable, setup

if __name__ == "__main__":
    setup(
        name="SECOR",
        version="1.0",
        description="Security Environment Configuration Orchestrator",
        executables=[Executable(script="main.py", target_name="SECOR_v1.0")],
    )
