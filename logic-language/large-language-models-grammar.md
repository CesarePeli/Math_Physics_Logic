---
layout: default
date: 2026-09-01
title: "Do Large Language Models Learn Grammar?"
author: Andrea Padovan
permalink: /logic-language/large-language-models-grammar/
background_image: "/images/LLM.png"
description: "How do large language models learn grammar? A comparison of LLM tokenization, embeddings, attention, and human language acquisition."
area: logic-language
content_type: article
---

<div class="content-box">

## Do Large Language Models Learn Grammar?

*By Andrea Padovan*

Who among us is unfamiliar with large language models? Whether ChatGPT, Claude, Gemini, Llama, DeepSeek, or others, most people have interacted with these systems at least once. Calling them “chatbots” would be reductive, since this label does not reflect their remarkable internal complexity or the variety and accuracy of their responses.

Let us begin with the fact that these models are called “language” models because they interact with users by encoding linguistic strings as input—during training, *fine-tuning*, through prompts, and so on—and producing linguistic strings as output: that is, what the model actually “says.” The verb *say* appears in quotation marks because, from the perspective of linguistics as the discipline that studies human languages, one of the central questions is how to understand the grammatical nature of the linguistic strings produced by a model. How can a model learn a language without—as far as we know—receiving explicit grammatical instruction, solely by being trained on millions upon millions of lines of text from books, websites, magazines, and other sources? Is the grammar learned by a model—that is, the set of abstract rules that make it possible to construct sentences and longer texts—comparable to the grammar acquired by a child exposed to the native language spoken by the people around them?

As a first approximation, our intuitive idea of a language is that it consists of sentences used for many different purposes: making requests and statements, asking questions, giving orders, and so forth. What is a sentence made of? Again, intuitively, we can say that it is made of words. As children, we are exposed to words and sentences and gradually learn to combine them as the grammar of our language is internalized by the brain.

It is difficult to imagine that the same process applies to LLMs. First of all, LLMs do not process words directly as meaningful units: they convert tokens into *embeddings*, numerical vectors with many dimensions. In a deliberately simplified example, we might imagine words such as *dog* and *puppy* being represented by simple vectors: *dog* might correspond to [1, 0] and *puppy* to [1.2, 0.1]. Because the two vectors are very similar and occupy nearby positions in this space, the model can treat the two terms as semantically related. In real applications, of course, embeddings do not have only two coordinates, but hundreds or thousands of dimensions, and the meaning of each dimension generally cannot be interpreted in isolation.

These representations are learned from the statistical regularities found in texts: words, fragments of words, and other tokens—which may correspond only to parts of words, punctuation marks, or other textual units—that occur in similar contexts tend to acquire similar vector representations. The proximity between *dog* and *puppy*, therefore, does not arise because the model necessarily possesses a concept of “dog” analogous to the human one. It arises because the two elements frequently occur in similar linguistic contexts and enter into predictable relations with many other expressions—hence their “proximity” within a particular representational space.

Embeddings thus allow the model to organize linguistic elements within a mathematical space in which certain relations can be expressed as distances and directions. This structure enables it to recognize associations and contexts and to produce plausible linguistic sequences. Such an ability should not be confused with genuine semantic understanding or with knowledge of the world comparable to that of human beings: embeddings primarily represent distributional relations learned from data.

Moreover, as already noted, what is encoded does not always coincide with whole words, but with what we have defined as tokens. A word such as *puppies* may be represented as a single token, divided into *pupp* + *ies* or *p* + *uppies*, or split into other fragments, depending on the tokenization system. This system of encoding is entirely unlike the way humans process language. We should also remember that children learn words in a multisensory environment made up of situations, sensations, and often emotions.

We can now turn to the question of how words are “put together” to form sentences. LLMs learn grammar through exposure to enormous quantities of text. By learning to predict the next token, they acquire syntactic and semantic-pragmatic regularities. Here too, the process appears to differ from human language acquisition: the human mind organizes sentences into hierarchical structures, or phrases, and establishes relations even between distant elements—between nouns and pronouns, for example, or between interrogative expressions and the verbs that license them—instead of proceeding through simple linear sequences. Predicting the next token is not, by itself, enough to explain a grammatical competence comparable to the human one.

When treating sentences as hierarchical structures composed of phrases, the human mind recognizes long-distance relations. In subject–verb agreement, for example, the verb does not necessarily agree with the nearest noun. In *The musician plays in the theatre*, the verb agrees with *the musician*. In *The girls who know the musician play in the theatre*, however, *play* agrees with the main subject, *the girls*, rather than with the nearer noun *the musician*, which belongs to the relative clause and is therefore part of a structure subordinate to the main clause. This simple example shows that human grammar recognizes the different structural roles of words and establishes relations over a distance.

LLMs, by contrast, were originally developed as systems that probabilistically estimate which element should follow a given sequence. It would be incorrect to claim that an LLM cannot reconstruct long-distance relations. Thanks to the mechanism of *attention*, LLMs can also build a network of relations among words. Attention allows a model to consider many other tokens in the context when processing a particular token, rather than looking only at the immediately preceding one, and thus to determine which are most relevant—from a syntactic viewpoint or otherwise—at that point in the sentence. Complex as this mechanism is (see Vaswani et al. 2017), it does not demonstrate that these models process grammar in the same way as the human brain, at least according to formal approaches to grammar such as Generative Grammar, developed by Noam Chomsky and many other scholars from the second half of the twentieth century onwards.

The relationship between LLMs and grammar has prompted a heated debate within theoretical linguistics. According to some scholars, LLMs are sophisticated “stochastic parrots,” unsuited to serving as models of the human language faculty. Others argue that these models show how complex grammatical competence can emerge from exposure to data alone. The distance from human language acquisition nevertheless remains considerable, even in purely quantitative terms: training a model requires billions of words, compared with the millions sufficient for the linguistic “training” of a child. LLMs also operate on tokens determined according to computational criteria, which do not necessarily coincide with the linguistic units recognized by the human mind.

</div>

<div class="content-box">

## Bibliography

- Chomsky, Noam, Ian Roberts, and Jeffrey Watumull. 2023. “Noam Chomsky: The False Promise of ChatGPT.” *The New York Times*.

- Piantadosi, S. 2024. “Modern Language Models Refute Chomsky’s Approach to Language.” In *From Fieldwork to Linguistic Theory*, 353–414. Language Science Press. [https://doi.org/10.5281/zenodo.12665933](https://doi.org/10.5281/zenodo.12665933).

- Vaswani, Ashish, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. 2017. “Attention Is All You Need.” In *Advances in Neural Information Processing Systems 30*, 5998–6008.

</div>

<div class="content-box">

## About the Author

**Andrea Padovan** is Associate Professor of German Language, Translation and Linguistics at the University of Verona. His research interests include language learning and processing, theoretical linguistics, and computational linguistics.

</div>
