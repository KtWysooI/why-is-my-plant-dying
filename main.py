import streamlit as st

#So, the idea for this project is: an app that clearly explains to novices/laypeople why their plant is dying

#To do:
#differentiate between indoor/outdoor setting
#bushes?
#divide between has/should have flowers, leafy, succulent
#determine time of year (which season)
#have tips about which colors needs/behaviors differ
#fertilizer check - have explanation of what to do?
#watering check - how often and how much
#    need to explain here too
#how to get soil into the pot or how many plants should be in certain pots
#ability to select flower based on picture (state to ignore coloring)
#    rearrange to place the ones in season first
#ask if they know what the plant is
#include warnings if plants are poisonous (pointsettias)
#include warnings if plants may irritate skin (zinnias)
#include warnings if plants have care specific to them (african violets)
#include special mention which plants seem to attract more bees
#include special mention if edible (nastrium) or if not (cabbage and kale)
#how to deadhead
#how to dispose of plant/pot afterwards
#to scale, will need information about plants outside of maryland 
#   will only truly be accurate to dmv area based on seasons and weather
#for outside, rain, wind, when to water
#need functionality to go all the way back to the beginning whenever
#   also functionality to go back just 1 page

#tkinter package

def fix_problem(p):
     st.write('The problem is : ', p)

     if (p == '--'):
          st.write(p)
     elif (p == 'is massively drooping'):
          st.write("You're already aware it needs water right now.")
          st.write('An additional note is the you should NOT fertilize plants when they are very dry like this.')
          st.write('They absorb the fertilizer too fast and burn themselves.')
     elif (p == 'leaves are yellow or paper-thin and shrivelly'):
          st.write('Plant needs more water.')     
          #have water tutorial link, reminder no fertilizer
          #also take into consideration the season
     elif (p == 'leaves are brown'):
          st.write('Those leaves are dead.')
          st.write('Remove them from the plant.')
          st.write('Dead leaves will take up resources from the plant that could be used to make new leaves.')
          st.write('You should be able to remove the leaf by hand. Use your fingernails or twist at the stem of the leaf to help.')     
     elif (p == 'some branches are brown but some are green, main stem is still green'):
          st.write('Remove the dead branches (the brown ones).')
          #have deadheading tutorial
     elif (p == 'whole or majority of main stem is brown'):
          st.write('It is dead. Mourn it. Chuck it.')
          #need additional consideration for annual vs perennial
          #also, need post mortem on what went wrong
     elif (p == 'leaves have holes'):
          st.write('')
          #determine if cat or bug or rodent
     elif (p == 'stem is bent or plant is falling over'):
          st.write('If the overall plant is bent; get a chopstick or stake based on the plant\'s size, or plant ring support, and string or twine.')
          st.write('Pull the majority of the plant upright and tie it to the support with the string. Tie the string around a major branch or the main stem.')
          st.write('A still growing plant will actually begin to grow into that straightened shape, and if it doesn\'t, it\'ll still keep it from falling over.')
          st.write('This may be from the following reasons: the stem is just crooked, growing fruit got too heavy and is pulling the plant over, it was knocked over by wind or other means and has bent or grown bent, etc.')        
     elif (p == 'is too small'):
          #get a feel if its early
          st.write('The plant may be hungry. Follow the fertilizing tutorial.')
          #do tutorial on fertilizing, remember snaps need half
     elif (p == 'there are no flowers or too small flowers'):
          #figure out if early or late in season
          st.write('')     
          #Explain how need nitrogen in fertilizer
     elif (p == 'weeds or another plant growing up by or through plant'):
          st.write('')
     else:
          st.write("You can't fix those.")
          st.write('\nIf the burn marks are on the leaves, and only a small bit of the leaf, just leave it attached.')
          st.write('If the burn marks are on the majority of a leaf, remove the leaf.') 
          st.write('The same directions go for flower petals.')
          st.write('If the burn mark is on the stem, but the stem is green, leave that alone.')
          st.write('If the stem is extensively damaged, try to remove just that one branch. See deadheading tutorial.')
          st.write("\nNow, you may be wondering, 'my plant hasn't been near any fire. How could it have burned?'")
          st.write('The answer is: the sun.')
          #find out if african violet, explain issues with them
          st.write('The sun beats down on everything and that includes your watering can, gardening hose, and plant.')
          st.write('Despite the advice on the interwebs that plants like warm water, 1. they, like humans, enjoy cold water on warm days and 2. they scald with hot water.')
          st.write("Before using water on your plant, quickly test it with your hand (carefully) to make sure it isn't hot. If it doesn't hurt, it's fine.")
          st.write('For the plant itself, if it gets too dry and is then fertilized, it will actually pull the fertilizer in so fast that it burns itself with it.')

#################################

st.title('Welcome to \"Why is my plant dying?\"')
st.write('\nThis app is for laypeople who like plants, but also have lives and just want the plant to not die.')
st.write('Please answer some questions about your plant problem for help.')

#Change selectbox to have is any part of it yellow or brown
#Then if selected, have slider for how bad the issue is
problem = st.selectbox(
     'What is the main problem?',
     ('--', 'is massively drooping', 'leaves are yellow or paper-thin and shrivelly', 'leaves are brown', 'some branches are brown but some are green, main stem is still green', 
          'whole or majority of main stem is brown', 'leaves have holes', 'stem is bent or plant is falling over', 'is too small', 
          'there are no flowers or too small flowers', 'weeds or another plant growing up by or through plant', 'plant has burn marks')
)

fix_problem(problem)

st.write('\nNo problem or need information about plant care?\nHit one of the buttons to read the guide on that subject.')

btn_wtr = st.button('Watering')

if btn_wtr:
     st.write('this is the watering tutorial')

st.write('\nWant additional notes specific for this plant? Click the button under its picture for more.')

#month = st.selectbox(
#     'What month is this?',
#     ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'))

#st.write('You selected:', month)

#is_inside = st.selectbox(
#     'Is this plant indoors?',
#     ('Yes', "No")
#)

#if is_inside == 'No':
#     st.write('It is dead because it is winter. Please wait for spring.')

#if st.button('Say hello'):
#     st.write('Why hello there')
#else:
#     st.write('Goodbye')

#from datetime import datetime
#start_time = st.slider(
#     "When do you start?",
#     value=datetime(2020, 1, 1, 9, 30),
#     format="MM/DD/YY - hh:mm")
#st.write("Start time:", start_time)     
