# run_in_executor

# import asyncio
# import time

# async def function_1(sec):
#   print(f"{sec} Waiting")
#   loop = asyncio.get_running_loop()
#   await loop.run_in_executor(None, time.sleep, sec)
#   return f"success {sec} minute waiting"

# async def main():
#   print(f"main start{time.strftime('%X')}")
#   task1 = asyncio.create_task(function_1(1))
#   task2 = asyncio.create_task(function_1(2))
#   await task1
#   await task2
#   print(f"{task1.result()}")
#   print(f"{task2.result()}")
#   print(f"main fin{time.strftime('%X')}")

# if __name__ == "__main__":
#   asyncio.run(main())

# import asyncio
# import time

# async def function_1(sec):
#   print(f"{sec} Waiting")
#   await asyncio.sleep(sec)
#   return f"success {sec} minute waiting"

# async def main():
#   print(f"main start{time.strftime('%X')}")
#   try:
#     result = await asyncio.wait_for(function_1(10), timeout=3)
#     print(result)
#   except asyncio.TimeoutError:
#     print("Time Out")
  
#   print(f"main fin{time.strftime('%X')}")

# if __name__ == "__main__":
#   asyncio.run(main())

# File DownLoad (Azure Ver)

# import asyncio
# import time
# from const import CONNECT_STR
# from azure.storage.fileshare.aio import ShareFileClient

# async def download(file):
#   file_client = ShareFileClient.from_connection_string(
#     conn_str=CONNECT_STR,
#     share_name="supu-test",
#     file_path=file,
#   )
#   with open(file, "wb") as file_handle:
#     data = await file_client.download_file()
#     await data.readinto(file_handle)
#   await file_client.close()

# if __name__ == "__main__":
#   asyncio.run(main())