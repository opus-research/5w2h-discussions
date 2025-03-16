import numpy as np
from openai import OpenAI

#Add here the key of ChatGPT
#  INSERT THE KEY client = OpenAI(api_key=)


def get_completion(
        messages: list[dict[str, str]],
        model: str = "gpt-4o",
        max_tokens=500,
        temperature=0,
        stop=None,
        seed=123,
        tools=None,
        logprobs=None,
        top_logprobs=None,
) -> str:
    params = {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "stop": stop,
        "seed": seed,
        "logprobs": logprobs,
        "top_logprobs": top_logprobs,
    }
    if tools:
        params["tools"] = tools

    completion = client.chat.completions.create(**params)
    return completion


def classify_text_with_completions(text):
    try:
        CLASSIFICATION_PROMPT = f""" 

        DEFINITION OF WHO:
        "should bring those responsible for the action"
        Full stack Jr. and Full Developers
        UX/UI Designer
        Test Analyst and Product Owner
        Test Analyst
        Every project ́s workers
        Who will solve the issue?
        Is this person getting attracted on it?
        Is this person feeling safe?
        Is it easy to work?
        Does this person have experience level?
        Does this person have the required skills?
	    Do negotiators receive support for their decisions?
	    How would you rate the decision according to probability? Risk decision?
	    How would this decision be classified according to the deadline? Short-Term Decision or Long-Term Decision?
	    Who is responsible for performing each action?
	    How can we improve the current form?

        DEFINITION OF WHAT:
        "brought the actions, the steps"
        Automated testing before code and code review.
        Inclusion of the Design Review column to check each component of the screen delivered by the Developer, check font size and compare parameters and components with the prototype.
        Time metrics for the correction of each bug which must start in accordance with the degree of criticality, not by the opening date.
        Holistic revision of the components of the prototype compared to the developed screen.
        Include the FDD as a small process within the agile. The development of projects through the application of Feature Driven Development, created by Jeff de Luca and Peter Coad in Singapore (SBROCCO, 2012, p.99) in the years 1997/1998, is considered an option for companies that act in an interactive and incremental way. However, it is necessary to maintain a pre-defined process. The methodology also recommends that a record is kept of every implementation, as follows: organized by functionality and dates, since the creation.
        What is the issue?
        What is the issue's description?
        What is the type of the issue?
	    What is considered when making the decision?
	    How to streamline the decision-making process?
	    What are the main difficulties in decision-making?
	    Is there any support tool for this decision-making?
	    What are the main logistical problems of this process?
	    Do negotiators receive support for their decisions?
	    What is the scope of this process?
	    What level of decision-making should the system handle?
	    Strategic Decision
	    Tactical Decision
	    Operational Decision
	    How is currently existing decision-making classified, programmed or non-programmed (or both)?
	    How would you rate the decision according to probability? Risk decision?
	    How would you rate the decision according to probability? Decision uncertainty?
	    How would you rate the decision according to probability? Sure decision?
	    What level of decision-making should the system handle?
	    How would this decision be classified according to the deadline? Short-Term Decision or Long-Term Decision?
 	    What is the cost involved in carrying out the process?
	    Where does the current system run?
	    Who is responsible for performing each action?
	    What is the frequency of carrying out this action?
	    How can we improve the current form?

        DEFINITION OF WHEN:
        "brought dates, deadlines and periodicities"
        During coding, the Developer uses the FDD before starting the task and after coding, completing the automated test.
        This column will be included after each task delivered by the developer and before the quality test. After that, the approved screen will be sent to the test analyst.
        When a bug is opened, the test analyst should communicate the PO who will determine the degree of priority and estimate the time of completion.
        At the time of manual testing.
        At Scrum ceremonies and Sprint development.
        When the issue was or will be solved?
        What is the deadline?
        Is it open, closed or ongoing?
        What is the description of the ongoing solution?
	    What is considered when making the decision?
	    Is there any support tool for this decision-making?
	    Strategic Decision 
	    Tactical Decision
	    Operational Decision
	    What level of decision-making should the system handle?
	    How is currently existing decision-making classified, programmed or non-programmed (or both)? 
	    How would this decision be classified according to the deadline? Short-Term Decision or Long-Term Decision?
	    What is the cost involved in carrying out the process?
	    Where does the current system run?
	    Who is responsible for performing each action?
	    What is the frequency of carrying out this action?
	    How can we improve the current form?

        DEFINITION OF WHERE:
        "brought location within the system architecture"
        In localhost and code development platform.
        Click up system in the current Sprint development - management and activity control tool. Click up in the Bug area - activity management and control tool.
        In the test approval area.
        Along the Sprint and management by the Click Up tool.
        Where is the issue?
        What is the start point?
        What are the connected areas?
        Where is it located in code?
	    What is the cost involved in carrying out the process?
	    Where does the current system run?
	    What is the frequency of carrying out this action?

        DEFINITION OF WHY:
        "brought justifications and reasons"
        The developer will have a revised code delivery through automated testing.
        The Designer will be able to do the revision and point out some faults before the test, making it less overloaded and preventing more bugs from opening.
        Greater control of the completion time of each bug, to decrease their accumulation at the end of Sprint.
        To have a more reliable check of the components that were previously unnoticed, decreasing bugs in the client.
        The use of FDD in a project recommends the application of a tool that allows the organization to adopt all the implementations that they want to create, enabling the inclusion and discrimination of all the necessary components for the new features (BARBOSA; 2008, p.10). Therefore, this will facilitate the understanding of the user stories and the business requirements, the inclusion of rule comments in the code and quality process improvements.
        Why it is an issue?
        What is the goal to solve it?
        What are the benefits of solving it?
        What are the expected behaviour?
	    How does the Negotiation Process work?
	    How to improve the decision-making process?
	    What are the main logistical problems of this process?
	    Do negotiators receive support for their decisions?
	    What is the scope of this process?
	    What level of decision-making should the system handle?
	    How is currently existing decision-making classified, programmed or non-programmed (or both)?
	    How would you rate the decision according to probability? Risk decision?
	    How would you rate the decision according to probability? Decision uncertainty?
	    How would you rate the decision according to probability? Sure decision?
	    What level of decision-making should the system handle?
	    What is the cost involved in carrying out the process?
	    How can we improve the current form?

        DEFINITION OF HOW:
    	"presented methods and processes"
        Automated testing training for Full stack Junior Developers.
        Including as a new task for the Project Designer.
        Assigning as a new process of control and management of the opening and correction of bugs.
        Including as a manual testing activity.
        Including as a second agile tool, through the verification of macro features and their user stories and inclusion of rules and comments in the code.
	    How does the Negotiation Process work?
	    How to improve the decision-making process?
	    How to streamline the decision-making process?
	    How is currently existing decision-making classified, programmed or non-programmed (or both)?
        How to solve the issue?
	    How to solve the issue?
	    What are the steps to reproduce?
	    What are the steps to Debug?
	    What is the scenario?
	    What are the previous attempts?
        What are the solving challenges?

        DEFINITION OF HOW MUCH:
        "brought cost data to the solution"
        How big is the issue?
        What is the required Effort? 
	    What is the cost involved in carrying out the process?
        You will be given GitHub messages that each message must be classified 
        into one of the 5W2H categories. MAKE SURE your output contains ONLY one of the 
        following categories: [who, what, when, where, why, how, how much]. Answer in lowercase.
        Text to classify: {text}
        """

        API_RESPONSE = get_completion(
            [{"role": "user", "content": CLASSIFICATION_PROMPT}],
            model="gpt-4o",
            logprobs=True,
            top_logprobs=4
            # NUMERO DE CLASSES A SE CONSIDERAR
        )

        classification = API_RESPONSE.choices[0].message.content
        top_logprobs = API_RESPONSE.choices[0].logprobs.content[0].top_logprobs

        class_probs = []
        for i, logprob in enumerate(top_logprobs, start=1):
            class_i = logprob.token
            class_i_prob = np.exp(logprob.logprob)
            class_probs.append((class_i, class_i_prob))

        return classification, class_probs
    except Exception as e:
        print("Error:", str(e))
        return None, None


#text_to_classify = input("Enter the text to classify: ")
#classification, possible_classes = classify_text_with_completions(text_to_classify)

#print(classification)
#print(possible_classes)
#print("------------------")
#print("")
