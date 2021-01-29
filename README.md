## preamble

*Gameit* is an intelligent gamification framework that accepts a set of predefined `rules` and uses a high level abstractural language to generates respective functions in Python-3.


## How does it work?

*Gameit* uses rules for constructing the functions, but what are rules? every rule contains a set of conditions and is defined by a logical relation between these conditions.

Conditions, in other hand are combination of attributes and operations which define a particular behavior for an entity.


In order to get the *Gameit* to work, you need to define three separate files so that it can use them for generating the functions. These three files are:

   - Methods
   - Awards
   - Rules

You can read the full documentation in doc directory.


## How good it is? 

![1aeef64ace58f6e66974ea7175a8f2c4](https://cloud.githubusercontent.com/assets/5694520/26025539/4ea235aa-37ff-11e7-8e65-62cf261703d8.jpg)


Well, all you need is writing your desired description regard a particular award in natural language and apply some simple tweaks to make it an understandable syntax for `Gameit`:


> I want to give `QuickLoyal` award to any user that paybacks in a group after someone's request less than N minute as the first person.

You can simply define your rule as following:

```
pay_back_rule = {
	cond1 = (payback.datetime - payack.payrequest_id.datetime) < time(h=3)
	cond2 = (count(payack.payrequest_id.pay_off) == count(payack.payrequest_id.involved_users))

	rule = cond1 and cond2
	award = "QuickLoyal"
}

```

----------

Note that you should have already defined the `Award_x` in `awards.json` file like following:

```
QuickLoyal = {
	point = 5
	badge = "QuickLoyal"
	privilege = None

	message = "Congratulations you got the 'QuickLoyal' badge!"
}

```

And following methods in `methods.json` file:

```
{

"payback": {
	"parent": "user",
	"attributes": {
		"pay_request_id":"int",
		"datetime":"datetime", 
		"amount":"float"},
},

"pay_rquest": {
	"parent": "user",
	"attributes": {
			"request_id":"int",
			"datetime": "datetime",
			"amount":"float",
			"involved_users":"list",
			"pay_off":"list"
			}
}

```
