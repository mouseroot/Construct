# Construct
Create energetic constructs.


```python
Absorber = Construct("Absorber")
Battery = Construct("Battery")
Absorber.program("Absorb ambient energy")
Battery.program("Store Energy")
Absorber.link(Battery)
Battery.link("Github Page: https://github.com/mouseroot/Construct")
Absorber.run()
```

The Absorber "absorbs ambient energy" and is linked to the Battery which "stores energy", the Battery is then linked to the page.
Then finally we run the construct and the page is loaded with the absorbed energy.
