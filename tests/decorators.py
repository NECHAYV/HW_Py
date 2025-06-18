# decorators.py
from datetime import datetime
from typing import Callable, Any, Optional
import functools


def log(filename: Optional[str] = None) -> Callable:


    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:

            func_name = func.__name__
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_message = f"[{timestamp}] {func_name}"

            try:
                result = func(*args, **kwargs)
                success_message = f"{log_message} ok\n"

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(success_message)
                else:
                    print(success_message, end="")

                return result
            except Exception as e:
                error_message = (
                    f"{log_message} error: {type(e).__name__}. "
                    f"Inputs: {args}, {kwargs}\n"
                )

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(error_message)
                else:
                    print(error_message, end="")
                raise

        return wrapper

    return decorator