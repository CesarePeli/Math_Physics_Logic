---
layout: default
date: 2025-08-30
title: "Solved Exercises — Sequences"
meta-description: "Solved exercises on recursive sequences: step-by-step proofs with monotonicity and boundedness, fixed-point equations, subsequences, and full author arguments."
permalink: "/university/math/calculus-1/sequences/"
background_image: "/images/serie.png"
---

<div class="content-box">

## Theoretical Recall

A **sequence** is a function $a:\mathbb{N}\to\mathbb{R}$, written $(a_n)_{n\in\mathbb{N}}$.  
We only consider limits as $n\to +\infty$.

- **Convergence:** $a_n\to L$ if $\forall\varepsilon>0\,\exists N:\ n>N\Rightarrow |a_n-L|<\varepsilon$.  
- **Divergence to $\pm\infty$** and **oscillation** as usual.  
- **Monotonicity:** increasing if $a_{n+1}\ge a_n$, decreasing if $a_{n+1}\le a_n$.  
- **Monotone Convergence Theorem:** every bounded monotone sequence converges.

We focus here on **recursively defined sequences**, where the $n$-th term depends on previous ones. Their behavior depends critically on the initial values.

</div>

<div class="content-box">

## Exercises

### Exercise 1  
$$
\begin{cases}
a_1=-\tfrac{3}{2},\\
a_{n+1}=a_n^2+4a_n+2
\end{cases}
$$

**Solution:**  
[Author’s full proof: monotonicity + induction + fixed point equation]  
**Final result:**  
$$\lim_{n\to\infty} a_n = -2.$$

---

### Exercise 2  
$$
\begin{cases}
a_1=2,\\
a_{n+1}=2\sqrt{a_n}
\end{cases}
$$

**Solution:**  
Increasing and bounded by $4$, convergence by Monotone Theorem.  
Limit equation $\ell=2\sqrt{\ell}$, roots $\ell=0,4$; only $\ell=4$ admissible.  
**Final result:**  
$$\lim_{n\to\infty} a_n = 4.$$

---

### Exercise 3  
$$
\begin{cases}
a_1=5,\\
a_{n+1}=\dfrac{a_n}{\tfrac12+a_n}
\end{cases}
$$

**Solution:**  
Decreasing, bounded below by $1/2$. Limit equation $\ell=\ell/(\tfrac12+\ell)$ → $\ell=0$ or $\tfrac12$.  
Admissible $\ell=\tfrac12$.  
**Final result:**  
$$\lim_{n\to\infty} a_n=\tfrac12.$$

---

### Exercise 4  
$$
\begin{cases}
a_1=\tfrac12,\\
a_{n+1}=a_n^3
\end{cases}
$$

**Solution:**  
Bounded in $[0,1]$, decreasing, so convergent. Limit equation $\ell=\ell^3$, roots $0,1,-1$; only $0$ admissible.  
**Final result:**  
$$\lim_{n\to\infty} a_n=0.$$

---

### Exercise 5  
$$
\begin{cases}
a_1=a>0,\\
a_{n+1}=\dfrac{a+a_n^2}{2}
\end{cases}
$$

**Solution:**  
Decreasing and bounded, convergence to $\ell$ solving $\ell=(a+\ell^2)/2$, i.e. $\ell=1\pm\sqrt{1-a}$.  
For $0<a<1$, admissible $\ell=1-\sqrt{1-a}$.  
**Final result:**  
$$\lim_{n\to\infty} a_n=1-\sqrt{1-a}, \quad 0<a<1.$$

---

### Exercise 6  
$$
\begin{cases}
a_0=\alpha\ge0,\\
a_{n+1}=a_n^2-a_n+1
\end{cases}
$$

**Solution:**  
Always positive, increasing. Limit equation $\ell=\ell^2-\ell+1$ → $\ell=1$.  
- If $\alpha<1$: bounded, so $\lim a_n=1$.  
- If $\alpha=1$: constant sequence $1$.  
- If $\alpha>1$: monotonicity forbids $\ell=1$, so $\lim a_n=+\infty$.  

---

### Exercise 7  
$$
\begin{cases}
a_1=\tfrac12,\\
a_{n+1}=\dfrac{1}{4-a_n}
\end{cases}
$$

**Solution:**  
Sharp bounds $2-\sqrt3 \le a_n \le 2+\sqrt3$.  
Monotone decreasing and bounded, so convergence. Limit equation $\ell=1/(4-\ell)$ → $\ell=2\pm\sqrt3$.  
Admissible root: $\ell=2-\sqrt3$.  
**Final result:**  
$$\lim_{n\to\infty} a_n=2-\sqrt3.$$

---

### Exercise 8  
$$
\begin{cases}
a_0=\tfrac34,\\
a_{n+1}=\dfrac{2a_n^2+1}{4a_n}
\end{cases}
$$

**Solution:**  
Decreasing and bounded below by $\tfrac{\sqrt2}{2}$.  
Limit equation $\ell=(2\ell^2+1)/(4\ell)$ → $\ell=\pm \tfrac{\sqrt2}{2}$.  
Positive root admissible.  
**Final result:**  
$$\lim_{n\to\infty} a_n=\tfrac{\sqrt2}{2}.$$

---

### Exercise 9  
$$
\begin{cases}
a_0=3,\\
a_{n+1}=\dfrac{8}{a_n^2}
\end{cases}
$$

**Solution:**  
Even/odd subsequences:  
- $(a_{2n})$ increasing $\to+\infty$,  
- $(a_{2n+1})$ decreasing $\to0$.  
Therefore the global limit does not exist.  

---

### Exercise 10  
$$
\begin{cases}
0<a_0<\pi,\\
a_{n+1}=a_n+\sin a_n
\end{cases}
$$

**Solution:**  
Increasing, bounded above by $\pi$. Limit equation $\ell=\ell+\sin\ell$ → $\sin\ell=0$, so $\ell=0$ or $\pi$.  
Admissible: $\ell=\pi$.  
**Final result:**  
$$\lim_{n\to\infty} a_n=\pi.$$

</div>

---

<div class="content-box">

## Explore more topics in Calculus 1

- [Complex Numbers]({{ "/university/math/calculus-1/complex-numbers/" | relative_url }})  
- [Notable Limits](/university/math/calculus-1/notable-limits/)  
- [Limits with L’Hôpital’s Rule](/university/math/calculus-1/limits-hopital/)  
- [Limits with Taylor Expansions](/university/math/calculus-1/limits-taylor/)  
- [Series](/university/math/calculus-1/series/)  
- [Continuity](/university/math/calculus-1/continuity/)  
- [Differentiability](/university/math/calculus-1/differentiability/)  
- [Integration by Parts](/university/math/calculus-1/integration-by-parts/)  
- [Integration by Substitution](/university/math/calculus-1/integration-substitution/)  
- [General ODEs](/university/math/calculus-1/odes-general/)  
- [Cauchy Problems for ODEs](/university/math/calculus-1/odes-cauchy/)  

</div>
