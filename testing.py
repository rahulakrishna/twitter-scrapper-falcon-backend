# Sneek peek on the results.
# Importing sentiment_mod module and then testing on some feeds and statements.

import sentiment_mod as senti

print(senti.sentiment("He is an incapable person. His projects are totally senseless."))
print(senti.sentiment("He is a freak."))
print(senti.sentiment("All did very well. All together a nice experience."))
print(senti.sentiment("Are you mad ?"))
print(senti.sentiment("You are dumb."))
print(senti.sentiment("This is pretty bad."))
