# Rules

Rules in Gamit are defined by a set of conditions and logical operations, which should be defined based on following structure:

```
Rule_X: {
	condition_1: "method.attr op vale|method.attr",
	condition_2: ...,
	...
	rule: "(condition_1 op condition_2) op ...",
	award: ...,
	type: "progressive|one-off"
}

```
