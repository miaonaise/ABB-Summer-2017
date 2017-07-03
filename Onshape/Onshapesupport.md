**Julia Li Jun 28, 11:07 UTC**
Hi,

I hope I have come to the right place. I am looking into creating a geometry with python scripting. I am hoping to get a library with Onshape modules to achieve an STL file in the end by running my python script. If I have not misunderstood, I will need an API-Key. I am new to this, hopefully I can achieve this with Onshape.

Regards, Julia
##
**mark_noyes (Onshape Support)**

Jun 28, 11:35 UTC

Yes, you should be able to do what you want. I am not clear on what stage you are at with Onshape development so I will give you a high level outline and you can go from there. To begin, you need to have "Developer Role" assigned. Just go to the developer portal (https://dev-portal.onshape.com) and accept the terms of use. Inside the developer portal you have access to detailed help topics for development, an interface for creating API keys, and interfaces to allow creating OAuth-based applications (which it doesn't seem like you need). You should begin by reading the API overview help section The sample applications include one called apikey, which includes python sample code. Note that it is not a complete python API, but includes a simple framework for python API requests with several API method wrappers implemented. The specific methods you want to call might not be implemented yet, but it is pretty easy to extend it. You will want to get the API Explorer from the App Store to fine out the details on the available APIs. If you have additional questions, feel free to post them here.
##
**Julia Li**

Jun 28, 16:10 UTC

Hi,

Thanks for the reply. I apologize for not understanding. I am not familiar with the concept of API, I checked the samples on github but I don't understand them. This is how I imagined to produce my geometry: Open python editor - write commands - run - an exported STEP/STL file appears in a directory. (I achieved this with FreeCAD, but their software is almost based on python which made is easier to find sample scripts.) From your response, it seems like I need to have skills of a developer to do something with Python API which I am not sure how it would help me with creating my geometry.

I would be thankful if you could tell a little more about this whole system for me.

Regards, Julia
##
**mark_noyes (Onshape Support)**

Jun 28, 17:25 UTC

A possible flow of a program that does what you want is:
1. Create a document using Documents - Create Document
2. Create a new Part Studio in the document using Part Studios - Create Part Studio
3. Add features to the Part Studio using one or more calls to the Part Studios - Add Feature API
4. Export the Part Studio to STL or STEP using the Part Studios - Export Part Studio to STL API or the Part Studios - Create Translation API

In Onshape, geometry is created by adding features to a Part Studio feature list. From there, parts can be exported or they can be put together into an assembly and the assembly exported.

The capabilities of features are defined using our FeatureScript language. Onshape provides a rich library of useful features but any user can define new feature types beyond what is supplied by Onshape. There is a single API call in the Part Studios API group (Add Feature) that can create any type of feature but the caller must understand the feature definitions.

You should probably begin by familiarizing yourself with the part studio modeling process to understand how you would construct the geometry and then attempt to make your python program add features. The Feature list API section of the developer portal help discusses the details of this call and other related calls. The Part Studios - Get Feature List API will send you back the contents of an existing feature list, allowing you to see the feature structure.

The apikey python sample is very limited, but provides a basic framework for extension. The app.py script will give you something to start from. You will need to extend apikey/client.py to implement missing calls to the API.
