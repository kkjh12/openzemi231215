# openzemi

This week’s assignment was to create an AI based application using the GPT 4 API. 
Our group started the assignment with the goal of innovating fintech with the API, by constructing an application that can read stock chart images and provide basic investment analysis for the public

GPT 4 is the fourth **multimodal language model** created by OpenAI. It was initially released earlier this year, and has been made publicly available via paid chatbot product and via OpenAI’s API. 
If anyone here is paying around $20 every month on Chat GPT, he/she would have access to GPT4. 

Now, there are many models of gpt4 available. The two newest ones are GPT-4 Turbo and GPT-4 Turbo with vision. 

There’s GPT-4 Turbo
- The latest GPT-4 model with improved instruction following, JSON mode, reproducible outputs, parallel function calling, and more.

And the model we used is GPT-4 Turbo with Vision. 
- Ability to understand images, in addition to all other things available on GPT-4 Turbo. 
- Since our goal is to make an application that is capable of understanding and interpreting stock images, this model is the most suitable compared to all other GPT4 models.


## Prompt Engineering
What our group prioritized when constructing the application was prompt engineering, which is probably one of the most crucial part of using the GPT4 API. 
You may ask “So what do you mean by prompt engineering?”
What I mean by prompt engineering is the process of “Crafting specific and structured questions or commands to effectively guide AI responses.”
Think of when you use chatgpt. Based on the way you ask, you can expect different answers with different qualities right? That’s why it’s important. 
When you write the prompts, you should consider the GPT-4’s inherent limitation that comes from OpenAI’s use-case policy. OpenAI's usage policies explicitly prohibit using its models for offering tailored financial, investment, or legal advice without a qualified person reviewing the information.

The prompt instructs the GPT-4 model to act as a financial analyst with risk assessment expertise. It requests a detailed examination of the uploaded stock chart image, providing a comprehensive explanation of its contents, including stock price movement, trends, volume, and potential market signals. The prompt is crafted to elicit a response that includes investment advice tailored for different investor types—risk-averse, risk-loving, and risk-neutral.

**First Application**
Now, based on the initial prompt I just explained, we designed our first application to analyze individual stock charts. 

**Second Application**
We expanded our capabilities beyond analyzing a single chart image. Our second application enables users to upload two images for comparative analysis. It builds upon the first application's capabilities to perform a comparative analysis of two different stock charts. 
The prompt is more complex; it requires individual analysis of each stock chart, followed by a comparison and contrast of the two stocks' performance. The AI is guided to highlight differences and similarities in patterns, trends, volume, and technical indicators, determining which stock appears to perform better based on historical patterns. This comparative analysis is framed within the context of providing educational insights, adhering to guidelines against giving specific financial advice.

## Future Possibilities
From the applications, we came up with some ideas for future development of applications
- First is to enable the analysis of more than two images simultaneously, offering a more intricate and detailed comparative analysis. This feature will allow users to gain a broader market perspective by comparing several stocks at once.
- Second is to use AI to make numerical assumptions drawn from images. This process includes estimating returns based on trends and patterns in stock charts, assessing risk from price movement variability, 
- Once the estimates are drawn from images, we can use these estimates to create an optimized portfolio, possibly employing a simplified version of the Efficient Frontier model. We could apply portfolio optimization algorithms like Mean-Variance Optimization. To deal with the uncertainties inherent in estimated data, and we could also employ Monte Carlo simulations, providing a more robust analysis and recommendations.

## Limitations
As introduced earlier, we have one clear inherent incompleteness caused by OpenAI’s use-case policy. This is kind of not avoidable but we can kind of avoid the restriction by writing a tricky prompt. 
The second limitation is that the future plans we came up with are all based on inferred data drawn from images. 
- The accuracy of this method is highly dependent on the quality of the image and the AI's interpretation capabilities.
- This method should not be used for real investment decisions without verification from actual historical data

# Get Access to Our Prototype
Unfortunately, we need more time to make the application publicly available, but we can give you access to the application if you give us your email. 
Either come to my computer and write your emails, or submit this form, and I’ll add you to the whitelist of our application. 
Link to form: https://forms.gle/rgo3xWYazvLBQ1oZ9 
- Once you submit the form, I'll add you to the whitelist of our application soon.
- Then, you'll receive an invitation from 'Databutton'
- You can easily access the prototype from there

# Caution
- Code are available in the github directory, BUT since we used an external software called 'Databutton' to make the prototype instead of Streamlit itself, the codes might need additional changes to be applied on Streamlit.
