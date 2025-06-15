'''
Here we can use predefined evaluators and also create our custom evaluator with a custom prompt.
https://pypi.org/project/openevals/0.0.11rc0/#conciseness
'''

from app.evaluation.chat_models import evaluator_model
from openevals.llm import create_llm_as_judge

from openevals.prompts import (
    CORRECTNESS_PROMPT,
    CONCISENESS_PROMPT,
    HALLUCINATION_PROMPT,
)


# Under-the-hood configurations 
_correctness_evaluator_fn = create_llm_as_judge(
    prompt=CORRECTNESS_PROMPT,
    judge=evaluator_model,
    feedback_key="correctness",
)

_conciseness_evaluator_fn = create_llm_as_judge(
    prompt=CONCISENESS_PROMPT,
    judge=evaluator_model,
    feedback_key="conciseness",
)

_hallucination_evaluator_fn = create_llm_as_judge(
    prompt=HALLUCINATION_PROMPT,
    judge=evaluator_model,
    feedback_key="hallucination",
)


# Public callable evaluators
def correctness_evaluator(inputs: dict, outputs: dict, reference_outputs: dict):
    return _correctness_evaluator_fn(
        inputs=inputs,
        outputs=outputs,
        reference_outputs=reference_outputs,
    )

def conciseness_evaluator(inputs: dict, outputs: dict):
    return _conciseness_evaluator_fn(
        inputs=inputs, 
        outputs=outputs
    )


def hallucination_evaluator(inputs: dict, outputs: dict, reference_outputs: dict):
    #get the context from inputs if available, otherwise default to an empty string
    context = inputs.get("context", "")
    return _hallucination_evaluator_fn(
        inputs=inputs, 
        outputs=outputs, 
        reference_outputs=reference_outputs,
        context=context,
    )