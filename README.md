# DiscordBot
*Contributors*
*Daniel Gresak*
*Vlad Rakhmanin (his idea)*

### Background
I decided to try make a bot that would read a sheet from Google Sheets and send a message if an assignment was dur within the next week.
I already had used the Sheety API so I copied the code from a previous project and made an Sheet with my college assignments and when it's due.

The project is a bit messy and was rushed but I think it's a cool addition to my classes discord.

### API's and Modules Used

I used the Sheety API to store the information on assignments. I thought that it would be the most accesable and easiest option for edits in the future.
I also used a discord webhook as the project didn't need a bot. If i decide to make it more reactive (e.g. adding assignments through discord) I may need to change 
that in the future. 

### Challenges

This is probably my first project that I implemented start to finish without it being an assignment or challenge. I decided to run it locally on my machine as
I was having difficulties installing the Discord module using python anywhere. Maybe it's possible to set it up to use Requests rather than the Discord Module. 

