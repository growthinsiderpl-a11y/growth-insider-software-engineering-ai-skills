#!/usr/bin/env python3
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _shared.tool_runtime import entrypoint

if __name__ == "__main__":
    entrypoint("validate_dependency_direction")
