# Richmond-Sausages-Hasbro-Competition-Loop
*Code is now redundant as the competition is over* Just posting this to show how badly the website was designed

# Backstory:
Richmond sausages ran a competition with Hasbro (the people who make monopoly etc) to give away some board games.

To enter the competition you went to competitions.richmondsausages.co.uk and entered a code which was found inside of a pack of sausages you purchased.

In short I found a way to make the site accept any code as a winner hence I could get as many prizes as I wanted until they caught on...

# The Loop:
I first of all began looking at different sources within the chrome developer console and found there was a file something like "app.js" and within that there was some code on how the page changed if your code was a winner > I found if I pasted this code within the chrome console it would put me on the winner page to enter my address however when I entered my address it was giving me an error saying my code was not a winner.

This was the "winner" code that would adjust the page:
```
$('.prize-area').fadeIn(1000).find('[data-prize="'+prize+'"]').show();
```
I found out that if you entered a code (even a random code that didin't match the format at all) and tried to enter it (and even if an error was returned from the code) it would then let you submit the "winner" (after you had tried to enter the random code) form with that code so in effect you could enter your own random codes and then use them to claim prizes.

After this I built the simple script I have put in this repository which uses the following sort of logic:
* Go to page
* Submit random code entery to make the code usable to claim a prize
* Submit winner form
* Success??
