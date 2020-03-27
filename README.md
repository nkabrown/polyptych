# Polyptych

**Suffering learning while under quarantine**

In _Picturing Quantum Processes_ the authors place their work as an attempt to understand quantum theory using pictures and processes instead of symbols and states. I'm intrigued. But I perhaps don't have the liberty of neglecting "symbols and states" since I'm up to my ears in conceptual debt. While under COVID-19 quarantine I'd like to set to work studying from both perspectives at once.

## Plan

```
 symbols and states                    mathematical machinery            pictures and processes
 ------------------                    ----------------------            ----------------------

 Mathematical Logic, Tourlakis     Graph Theory and its Applications     Picturing Quantum Processes

        ↓                                                                           ↓

 Theory of Sets, Bourbaki                                                New Structures for Physics

```

Goal: Build mathematical machinery and think about concepts

## Symbols and States

_Mathematical Logic_ G. Tourlakis

How is the relationship of logical languages to proving similar to the relationship of programming languages to programming?

Well, logical languages and programming languages are both artifical languages.

"As far as reading or writing a formalized text is concerned, it matters little whether this or that meaning is attached to the words, or signs in the text, or indeed whether any meaning at all is attached to them, the only important point is the correct observance of the rules of syntax." – _Elements of Mathematics: Theory of Sets_, Nicolas Bourbaki

What is the alphabet of Boolean logic?

What is the difference between variables and metavariables?

What are the definitions of strings and substrings?

What is the definition of formula-calculation?

What are the procedural and recursive definitions of the set WFF?

Write two parsing programs; a formula-constructor (build step-by-step) and a formula-deconstructor (recursively break down).

## Pictures and Processes

_Picturing Quantum Processes_ B. Coecke, A. Kissinger

The book uses a diagrammatic language to describe and reason about quantum theory. I'm quite interested in how I might use a diagrammatic language to describe and reason about programs and programming.

"...in diagrammatic theories, it is natural to treat arbitary processes on equal footing with states. States are then treated just as a special kind of process, a 'preparation' process. In other words, there is a shift from focussing on 'what is' to 'what happens', which is clearly a lot more fun. This is very much in line with the concerns of computer science, where the majority of time and energy goes into reasoning about processes (i.e. programs), and states (i.e. data) only exist to be communicated by programs." p.11-12

"We call a structure consisting of all the 'allowed processes' and how these interact a process theory." These process theories are defined as a category; a collection of types (objects), a collection of processes (morphisms), and a composition operation to join processes together. Process theories focus on composition, systems interacting with other systems, and have an interaction logic.

Nice description of seeking an abstraction: "As the standard, Hilbert-space presentation of the theory comes as a packaged deal, it is therefore necessary to seek an alternative presentation that lets us tease out the important features from the incidental ones." Diagrams are the abstraction they will use to drop incidental features and focus on the important features.

The definition of process theory is the definition of a category.

```
A process theory consists of:

(i) A collection T of system-types represented by wires,

(ii) A collection P of processes represented by boxes, where for each process in P the input types and output types are taken from T, and

(iii) a means of 'wiring processes together', that is, an opertation that interprets a diagram of processes in P as a process in P.

In particular, (iii) guarantees that process theories are 'closed under wiring processes together'.
```

Compare this to the definition of a category.

```
A category C consists of:

• A collection C₀, whose elements are called the objects of C and are usually denoted by uppercase letter X, Y, Z,...

• A collection C₁, whose elements are called the morphisms or arrows of C and are usually denoted by lowercase letters f, g, h,...

such that

• Each morphism has assigned two objects, called source and target, or domain and codomain. We denote the source and target of the morphism f by s(f) and t(f), respectively.

• Each object X has a distinguished morphism id(x) : X →  X, called the identity morphism.

• For each pair of morphisms f, g such that the t(f) = s(g) there exists a specifed morphism f ° g, called the composite morphism, such that s(g ° f) = s(f) and t(g ° f) = t(g).

These structures need to satisfy the following axioms.

• Unitality: for every morphism f : X →  Y, the compositions f ° id(x) and id(y) ° f are both equal to f.

• Associativity: for f : X →  Y, g : Y →  Z and h : Z →  W, the compositions h ° (g ° f) and (h ° g) ° f are equal.
```

## Mathematical Machinery

_Graph Theory and its Applications_ Gross, Yellen, Anderson

A Graph constructor should return a null graph and then the ADT of the Graph should provide a procedural way to build a graph.

What is the difference between an adjacency table and an incidence table? Is there a mapping that will transform one into the other?

Description of graph and its relation to logic from [Graph Structure and Monadic Second-Order Logic, a Language Theoretic Approach](https://hal.archives-ouvertes.fr/hal-00646514/document) "A graph can be considered as a _logical structure_ (also called _relational structure_) whose _domain_ (also called its _universe_) consists of the vertices, and that is equipped with a binary relation that represents adjacency." p. 5

- [ ] Read tutorial section on Python classes
- [ ] Create a Graph class with builder methods
- [ ] Create separate classes to utilize two different edge representations:
     - [ ] strings
     - [ ] tuples
- [ ] Write tests based on graph properties
- [ ] Return adjacency table as an actual table

Areas of application that I might wish to explore:

[Algorithmic Cheminformatics](https://cheminf.imada.sdu.dk/): Graph grammar chemistry where molecules are represented as graphs and chemical reactions as graph transformation rules.

* [Intro article](https://royalsocietypublishing.org/doi/pdf/10.1098/rsta.2016.0354)
* [From Category Theory to Enzyme Design](https://cheminf.imada.sdu.dk/novo-synergy/)

Influenza map from CDC or state data that returns closed neighborhoods of counties that are on an upswing.

![Yellow Jack Quarantine Flag](https://pbs.twimg.com/media/DkUciO0W0AAmkHM?format=jpg&name=240x240)

## Diary

Sickness is the law of the living.

Calling it the "Chinese Virus" hides the fact of our common humanity. "...the vision of the [stricken's suffering] could certainly still say a great deal to those who know how to look at it and do not recoil before what it shows of our common humanity."

How does internationalist solidarity compare to this biblical notion of common humanity?

"This may be an extinction event for small businesses and franchises." – Mike Davis

Note parallels between "flow" and one of the principles from Daniel Willingham's book _Why Don't Students Like School?_ that “People are naturally curious, but we are not naturally good thinkers; unless the cognitive conditions are right, we will avoid thinking.” I paraphrase the point of this principle as "Setting yourself up for success is important because you will only continue if your cognitve work is successful." While "flow [which occurs] when a person's skills are fully involved in overcoming a challenge that is just about manageable."
