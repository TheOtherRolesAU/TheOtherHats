![TheOtherHats Banner](./Images/TheOtherHats_logo.png)

# TheOtherHats
We're awaiting your creative hat designs and we'll integrate all the good ones in our mod  :heart_eyes:
Here are a few instructions, on how to create a custom hat:

### Hat Creation:
 A hat consists of up to three textures. The aspect ratio of the textures has to be 4:5, we recommend 300px x 375px.

### Main texture (required):
This is the main texture of your hat. It will usually be rendered in front of the player, if you set the behind parameter it will be rendered behind the player.
 The name of the texture needs to follow the pattern hatname.png, but you can also set some additional parameters in the file name by adding _parametername to the file name (before the .png).

**Parameter bounce:**
This parameter determines whether the hat will bounce while you're walking or not.

**Parameter adaptive:**
If this parameter is set, the Among Us coloring shader will be applied (the shader that replaces some colors with the colors that your character is wearing in the game). The color red (#ff0000) will be replaced with the primary color of your player and the color blue (#0000ff) with the secondary color. Also other colors will be affected and changed check out our GitHub page for more infos.

**Parameter behind:**
If this parameter is set, the main texture will be rendered behind the player.

### Climb texture (required):
This texture will be rendered in front of the player, when he's climbing.
The name of the texture needs to follow the pattern hatname_climb.png.

### Back texture (optional):
This texture will be rendered behind the player.
The name of the texture needs to follow the pattern hatname_back.png.

### Flipped texture (optional):
This texture will be rendered instead of the Main texture, when facing the left.
The name of the texture needs to follow the pattern hatname_flip.png.


### Template:
Feel free to download our template for Illustrator, Photoshop and PNG. It should help you to place your hat correctly. Note: Climbing assets can be a bit tricky since the crewmate moves from left to right while climbing. [(Links on our Discord)](https://discord.com/channels/818086884089659412/838414132776140800/838423406654914572)

### Testing:
You can test your hat design by putting all the files in the \TheOtherHats\Test subfolder of your mod folder. Then whenever you start a freeplay game, you and all the dummies will be wearing the new hat. You don't need to restart Among Us if you change the hat files, just exit and reenter the freeplay mode.

### Submission:
— Please do not submit hats from other mods or hats that contain licensed contents, we can't and won't add them.
— If you got a hat design, you can submit it on our [Discord](https://discord.com/channels/818086884089659412/838414132776140800/838423406654914572)
— You can submit a picture of how the hat looks like in game or you can submit the hat files themselves :wink:
