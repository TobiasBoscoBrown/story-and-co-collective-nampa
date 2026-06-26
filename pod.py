import asyncio, edge_tts, os
AVA="en-US-AvaNeural"; MARCUS="en-US-AndrewNeural"
lines=[
 (AVA,"Welcome back to The Find. I'm Ava."),
 (MARCUS,"And I'm Marcus. Today we're in Nampa, Idaho, at a boutique called Story and Co. Collective."),
 (AVA,"This one's a charmer. It's women owned, and it mixes brand new boutique fashions right in with curated consignment."),
 (MARCUS,"Which is the part I love. New and pre loved on the same rack. So every single visit, the floor looks different."),
 (AVA,"Their regulars figured that out. The trick isn't buying more, it's stopping in more often. New arrivals land most weeks."),
 (MARCUS,"And the designer bags move fastest. Think Michael Kors at a fraction of mall pricing. If you see one you love, put a hold on it."),
 (AVA,"That's the smart move. On their site you can build a list, add your name, and text it straight to the shop. Nothing's charged online."),
 (MARCUS,"They also share the floor with local Treasure Valley makers. Hand poured candles, tallow balms, jewelry, the little handmade things."),
 (AVA,"One reviewer called it the lovely smelly stuff. I think that's the highest compliment a candle can get."),
 (MARCUS,"And owner Megan leans into supporting local artists, which is just a nice way to shop."),
 (AVA,"So if you're in the Treasure Valley, swing by 134 South Midland Boulevard. Open Tuesday through Saturday."),
 (MARCUS,"Bring the clothes you've outgrown to consign, and leave with something new to you. That's The Find. See you next time."),
]
async def main():
    files=[]
    for i,(v,t) in enumerate(lines):
        f=f"seg_{i:02d}.mp3"
        await edge_tts.Communicate(t, v, rate="+6%").save(f)
        files.append(f)
    with open("concat.txt","w") as fh:
        for f in files: fh.write(f"file '{f}'\n")
asyncio.run(main())
print("segments done")
