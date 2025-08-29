---
layout: default
date: 2025-08-29
title: "Solved Exercises — Sequences"
meta-description: "Solved exercises on sequences (explicit and recursive): full step-by-step solutions with monotonicity and boundedness proofs, subsequences analysis, and complete author arguments."
permalink: "/university/math/calculus-1/sequences/"
background_image: "/images/euclide.png"
featured: true
---

<div class="content-box">

## Theoretical Recall

A **sequence** is a function $a:\mathbb{N}\to\mathbb{R}$, written $(a_n)_{n\in\mathbb{N}}$. We only consider limits as $n\to +\infty$.

- **Convergence:** $a_n\to L$ if $\forall\varepsilon>0\,\exists N:\ n>N\Rightarrow |a_n-L|<\varepsilon$.
- **Divergence to $\pm\infty$** and **oscillation** as usual.
- **Monotonicity:** increasing if $a_{n+1}\ge a_n$, decreasing if $a_{n+1}\le a_n$.
- **Monotone Convergence Theorem:** every bounded monotone sequence converges.

### Canonical examples
$\lim \frac1n=0,\quad \lim (1+\tfrac1n)^n=e,\quad \lim(-1)^n$ does not exist (oscillation),  
$\lim \sqrt[n]{n}=1,\quad \lim \frac{n}{\ln n}=+\infty,\quad \lim \frac{2^n}{n!}=0.$

</div>

<div class="content-box">

## Exercises

### Exercise 1 — Full induction bounds and limit equation
Let
$$
\begin{cases}
a_1=-\dfrac{3}{2},\\[2mm]
a_{n+1}=a_n^2+4a_n+2.
\end{cases}
$$

**Solution:**  
Show $a_{n+1}\le a_n$:
$$
a_n^2+4a_n+2\le a_n\iff a_n^2+3a_n+2\le0\iff -2\le a_n\le -1. \quad (4.3)
$$
Prove by induction the two bounds in (4.3):
- $p(n):\ a_n\ge -2$. Base $n=1$ is immediate. Inductive step:
  $a_{n+1}=a_n^2+4a_n+2\ge 4+4(-2)+2=-2$.  
- $b(n):\ a_n\le -1$. Base immediate. Inductive step:
  $a_{n+1}=a_n^2+4a_n+2\le 1+4(-1)+2=-1$.

Hence $(a_n)$ is decreasing, so $\lim a_n=\ell\in\mathbb{R}\cup\{-\infty\}$; with $-2\le a_n\le -1$ and decreasing we refine $-2\le \ell\le -\tfrac32$. Passing to the limit:
$$
\ell=\ell^2+4\ell+2\iff \ell^2+3\ell+2=0\iff \ell\in\{-2,-1\}.
$$
Exclude $\ell=-1$ by the refined bound. Thus
$$
\boxed{\lim_{n\to\infty} a_n=-2.}
$$
:contentReference[oaicite:0]{index=0}

---

### Exercise 2 — Increasing sequence with square-root recurrence
Let
$$
\begin{cases}
a_1=2,\\[2mm]
a_{n+1}=2\sqrt{a_n}.
\end{cases}
$$

**Solution:**  
For $a_n\ge0$,
$$
a_{n+1}\ge a_n \iff 2\sqrt{a_n}\ge a_n \iff 4a_n-a_n^2\ge0 \iff 0\le a_n\le4.
$$
Induce $a_n\le4$: $a_{n+1}=2\sqrt{a_n}\le 2\sqrt4=4$. Therefore $(a_n)$ is increasing and bounded, so $\lim a_n=\ell\in[2,4]$. Passing to the limit:
$$
\ell=2\sqrt{\ell}\iff \ell^2-4\ell=0\iff \ell\in\{0,4\}.
$$
Exclude $\ell=0$ by $\ell\ge2$. Hence
$$
\boxed{\lim_{n\to\infty} a_n=4.}
$$
:contentReference[oaicite:1]{index=1}

---

### Exercise 3 — Decreasing rational recurrence to a fixed point
Let
$$
\begin{cases}
a_1=5,\\[2mm]
a_{n+1}=\dfrac{a_n}{\tfrac12+a_n}.
\end{cases}
$$

**Solution:**  
Inductively prove $a_{n+1}\le a_n$ (base $10/11\le5$). Then $\lim a_n=\ell\in\mathbb{R}\cup\{-\infty\}$ with $a_n\ge \tfrac12$ so $\ell\ge\tfrac12$; since $(a_n)$ is decreasing and $a_1=5$, we have $\tfrac12\le \ell\le 5$. Passing to the limit:
$$
\ell=\frac{\ell}{\tfrac12+\ell}\iff \tfrac12\,\ell+\ell^2-\ell=0\iff \ell(\ell-\tfrac12)=0.
$$
Exclude $\ell=0$ by $\ell\ge\tfrac12$. Hence
$$
\boxed{\lim_{n\to\infty} a_n=\tfrac12.}
$$
:contentReference[oaicite:2]{index=2} :contentReference[oaicite:3]{index=3}

---

### Exercise 4 — Cubic contraction to zero
Let
$$
\begin{cases}
a_1=\tfrac12,\\[2mm]
a_{n+1}=(a_n)^3.
\end{cases}
$$

**Solution:**  
Show $a_{n+1}\le a_n$:
$$
a_n^3-a_n\le0\iff a_n(a_n^2-1)\le0\iff -1\le a_n\le 1.
$$
With $a_n\ge0$, we have $0\le a_n\le1$ and $(a_n)$ is decreasing; hence $\lim a_n=\ell\in[0,1/2]$. Passing to the limit:
$$
\ell=\ell^3 \iff \ell(1-\ell^2)=0 \iff \ell\in\{0,1,-1\}.
$$
Only $\ell=0$ is admissible. Thus
$$
\boxed{\lim_{n\to\infty} a_n=0.}
$$
:contentReference[oaicite:4]{index=4} :contentReference[oaicite:5]{index=5}

---

### Exercise 5 — Parameter-dependent quadratic mean
Let
$$
\begin{cases}
a_1=a>0,\\[2mm]
a_{n+1}=\dfrac{a+a_n^2}{2}.
\end{cases}
$$

**Solution:**  
Show $a_{n+1}\le a_n$:
$$
\dfrac{a+a_n^2}{2}\le a_n \iff a+a_n^2-2a_n\le0
\iff (1-\sqrt{1-a})\le a_n\le (1+\sqrt{1-a}). \quad (4.10)
$$
For $0<a<1$ the bounds are well-defined. Inductively:
- lower bound: $a_{n+1}\ge \tfrac12(a+1+1-a-2\sqrt{1-a})=1-\sqrt{1-a}$,
- upper bound: $a_{n+1}\le \tfrac12(a+1+1-a+2\sqrt{1-a})=1+\sqrt{1-a}$.  
Thus $(a_n)$ is decreasing and bounded, so $\lim a_n=\ell$ with $1-\sqrt{1-a}\le\ell\le 1+\sqrt{1-a}$. Passing to the limit:
$$
\ell=\frac{a+\ell^2}{2}\iff \ell^2-2\ell+a=0\iff \ell=1\pm\sqrt{1-a}.
$$
Since $(a_n)$ is decreasing and $a_1=a<1$, the admissible root is the smaller one:
$$
\boxed{\lim_{n\to\infty} a_n=1-\sqrt{\,1-a\,}\quad(0<a<1).}
$$
:contentReference[oaicite:6]{index=6}

---

### Exercise 6 — Quadratic map with cases on the initial datum
Let
$$
\begin{cases}
a_0=\alpha\in\mathbb{R}^+,\\[1mm]
a_{n+1}=a_n^2-a_n+1.
\end{cases}
$$

**Solution:**  
$(a_n)$ is positive since $x^2-x+1>0$. Show $a_{n+1}\ge a_n$:
$$
a_n^2-a_n+1\ge a_n \iff (a_n-1)^2\ge0.
$$
Hence $(a_n)$ is increasing and $\lim a_n=\ell\in\mathbb{R}\cup\{+\infty\}$. Limit equation:
$$
\ell=\ell^2-\ell+1\iff (\ell-1)^2=0\iff \ell=1.
$$
Case analysis:
- If $\alpha>1$, monotonicity forbids $\ell=1$; thus $\lim a_n=+\infty$.
- If $\alpha=1$, $a_n\equiv1$.
- If $0\le\alpha<1$, then $0\le a_n\le1$ and $\lim a_n=1$.
:contentReference[oaicite:7]{index=7}

---

### Exercise 7 — Reciprocal iteration with sharp bounds
Let
$$
\begin{cases}
a_1=\tfrac12,\\[2mm]
a_{n+1}=\dfrac{1}{\,4-a_n\,}.
\end{cases}
$$

**Solution:**  
Well-posedness: find $A>0$ with $4-a_n\ge A>0$. One gets
$$
2-\sqrt3\ \le\ A\ \le\ \tfrac72,\qquad\Rightarrow\qquad a_n\le 4-A\le 2+\sqrt3 \ \ \forall n\ge1.
$$
Monotonicity:
$$
a_{n+1}\le a_n \iff \frac{1}{4-a_n}\le a_n \iff \frac{a_n^2-4a_n+1}{4-a_n}\le0
$$
which holds for $2-\sqrt3\le a_n\le 2+\sqrt3$ (or $a_n>4$, excluded by base step). Inductively,
$a_n\le 2+\sqrt3$. A parallel argument shows $a_n\ge 2-\sqrt3$. Thus $(a_n)$ is decreasing and bounded, so $\lim a_n=\ell\in[\,2-\sqrt3,\tfrac12\,]$. Passing to the limit:
$$
\ell=\frac{1}{4-\ell}\iff \ell^2-4\ell+1=0\iff \ell=2\pm\sqrt3.
$$
By the bounds and monotonicity we select
$$
\boxed{\lim_{n\to\infty} a_n=2-\sqrt3.}
$$
:contentReference[oaicite:8]{index=8}

---

### Exercise 8 — A symmetric mean approaching $\boldsymbol{\tfrac{\sqrt2}{2}}$
Let
$$
\begin{cases}
a_0=\dfrac34,\\[2mm]
a_{n+1}=\dfrac{2a_n^2+1}{4a_n}.
\end{cases}
$$

**Solution:**  
Show $a_{n+1}\le a_n$:
$$
\frac{2a_n^2+1}{4a_n}-a_n\le0 \iff 1-2a_n^2\le0 \iff a_n\ge \frac{\sqrt2}{2} \ \text{ or } \ a_n\le -\frac{\sqrt2}{2}.
$$
Since $a_n>0$, keep $a_n\ge\frac{\sqrt2}{2}$. Inductively $a_n\ge\frac{\sqrt2}{2}$, and being decreasing we get
$$
\frac{\sqrt2}{2}\ \le\ \ell\ \le\ \frac34.
$$
Pass to the limit:
$$
\ell=\frac{2\ell^2+1}{4\ell}\iff 4\ell^2=2\ell^2+1\iff \ell=\pm \frac{\sqrt2}{2}.
$$
Only the positive root is admissible:
$$
\boxed{\lim_{n\to\infty} a_n=\tfrac{\sqrt2}{2}.}
$$
:contentReference[oaicite:9]{index=9} :contentReference[oaicite:10]{index=10}

---

### Exercise 9 — Even/odd subsequences with different limits
Let
$$
\begin{cases}
a_0=3,\\[2mm]
a_{n+1}=\dfrac{8}{a_n^2}.
\end{cases}
$$

**Solution:**  
Compute initial values to detect parity behavior, then analyze the even subsequence
$$
a_{2n+2}=\frac{8}{a_{2n+1}^2},\qquad a_{2n+1}=\frac{8}{a_{2n}^2}.
$$
From the derived inequalities one gets $a_{2n}$ increasing and unbounded ($\to+\infty$) while $a_{2n+1}$ decreasing to $0$. Therefore the full limit does not exist.
:contentReference[oaicite:11]{index=11} :contentReference[oaicite:12]{index=12} :contentReference[oaicite:13]{index=13}

---

### Exercise 10 — Increasing recurrence to $\boldsymbol{\pi}$
Let
$$
\begin{cases}
0<a_0<\pi,\\[2mm]
a_{n+1}=a_n+\sin a_n.
\end{cases}
$$

**Solution:**  
Use $\sin t<t$ for $t>0$ and $\sin a_n=\sin(\pi-a_n)<\pi-a_n$ to prove $0<a_n<\pi$ for all $n$ and $a_{n+1}>a_n$. Thus $(a_n)$ is increasing and bounded, so $\lim a_n=\ell\in(0,\pi]$. Passing to the limit:
$$
\ell=\ell+\sin\ell\iff \sin\ell=0\iff \ell\in\{0,\pi\}.
$$
Monotonicity and positivity exclude $0$, so
$$
\boxed{\lim_{n\to\infty} a_n=\pi.}
$$
:contentReference[oaicite:14]{index=14}

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
