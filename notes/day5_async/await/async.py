# async ka mtlb code ko fast krna nhi hota hai balki jb code wait kre toh kuch aur kaam kr lo.
# async.gather ka mtlb multiple async function ko ek sath run krna

import asyncio

async def task(name,delay):
    print(f"start {name}")
    await asyncio.sleep(delay)  #await bolta hai yaha ruk mat ,wait kr  
    print(f"end {name}")

async def main():
    await asyncio.gather(
        task("a",3),   #coroutine object A 
        task("b",3),    #coroutine object B
        task("c",3)     #coroutine object C 
                        #   abhi koi execution nhi hua h bss coroutine object bna h
    )    
asyncio.run(main())