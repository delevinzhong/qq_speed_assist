# import concurrent.futures
# import subprocess
#
#
# def run_program(program):
#     result = subprocess.run(
#         ['python', program],
#         stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE,
#         text=True
#     )
#     return program, result.returncode, result.stdout, result.stderr
#
#
# def run_double_mode():
#     program1 = "double_mode.py"
#     program2 = "take_screen_shot.py"
#
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         # Concurrently execute the programs using threads
#         futures = [executor.submit(run_program, program) for program in [program1, program2]]
#
#         # Wait for all tasks to complete
#         concurrent.futures.wait(futures)
#
#         # Process results
#         for future in futures:
#             program, returncode, stdout, stderr = future.result()
#             print(f"{program} exited with return code {returncode}")
#             print(f"stdout:\n{stdout}")
#             print(f"stderr:\n{stderr}")
#             print("------")


if __name__ == "__main__":
    run_double_mode()
