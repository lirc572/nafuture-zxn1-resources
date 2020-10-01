import uasyncio as asyncio
from machine import Pin

async def killer(duration):
    await asyncio.sleep(duration)

async def toggle(objLED, time_ms):
    while True:
        await asyncio.sleep_ms(time_ms)
        objLED.value(1 - objLED.value())

# TEST FUNCTION

async def main(duration):
    print("Flash LED's for {} seconds".format(duration))
    leds = [Pin(12, 1), Pin(2, 1)]  # Initialise 2 on board LED's
    for x, led in enumerate(leds):  # Create a task for each LED
        t = int((0.2 + x/2) * 1000)
        asyncio.create_task(toggle(leds[x], t))
    asyncio.run(killer(duration))

def test(duration=10):
    try:
        asyncio.run(main(duration))
    except KeyboardInterrupt:
        print('Interrupted')
    finally:
        asyncio.new_event_loop()
        print('as_demos.aledflash.test() to run again.')

test()
