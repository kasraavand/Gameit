#Methods

Methods are basically the column names of entities in a relational database. But still they can be a temporarily attributes of an entity.


## Structure

Methods are defined as follows:

```
method_name : {
	parent : X
	attributes : {
	    	attr1 : {
			type : X
	      	scope : (m, n)
	      	default : X  
	    }

	    	attr2 : {...}
	    	...

	       }
	description : X
}

```

Each method has a parent which is the respective entity name, and some attributes that denotes states of a method.

Here is an example:

```
shop : {
	parent : user
	attributes : {
			datetime : {
			type : "datetime"
			scope : (date(y=2016,m=01,d=01), None)
		}
			amount : {
			type : int
			scope : (0, 5M)
		}
}
}
```