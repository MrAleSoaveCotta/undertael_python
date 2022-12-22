import asyncio
import pg as pg

pg.init()

screen = pg.display.set_mode(1280,720)

async def main():

    running = True


    

        while running:

            for event in pg.event.get():

                if event.type == pg.QUIT:
                    running = False


            pg.display.update()

            await asyncio.sleep(0)
            if not running:
                pg

                

        

asyncio.run(main())