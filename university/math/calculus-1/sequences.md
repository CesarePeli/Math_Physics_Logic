---
layout: default
date: 2025-08-31
title: "Solved Exercises — Recursively Defined Sequences"
meta-description: "Ten selected recursive sequences: monotonicity, bounds, induction proofs, and fixed-point limits — each with a clean, step-by-step solution and the final limit isolated."
permalink: "/university/math/calculus-1/recurrence-sequences/"
background_image: "/images/sequences.png"
featured: false
---

<div class="content-box">

## Theoretical recalls

A sequence {aₙ} is a function a: ℕ → ℝ.  
The only accumulation point of ℕ in the extended real line ℝ ∪ {±∞} is +∞, so limits are always taken as n→+∞.

Key results:

- If {aₙ} converges, then it is bounded (the converse does not hold).  
- **Monotone convergence theorem.** A monotone and bounded sequence converges.  
- **Recursive sequences.** For k∈ℕ and f: ℕ × ℝ^{k+1} → ℝ:
  $$
  \begin{cases}
  a_{n+1}=f(n,a_n,\dots,a_{n-k}), & n\ge k,\\
  a_0,\dots,a_k\in\mathbb{R} & \text{(initial data)}.
  \end{cases}
  $$
Unlike explicit formulas, here each term depends on the previous ones; behavior depends critically on the initial values.

</div>

---

<div class="content-box">

## Worked Exercises

Below are ten selected recursive sequences. Each solution shows:  
- study of monotonicity and boundedness,  
- induction arguments when needed,  
- passage to the limit via the fixed-point equation,  
- final result isolated.

---

### Exercise 1
$$
\begin{cases}
a_1=-\tfrac{3}{2},\\
a_{n+1}=a_n^{2}+4a_n+2.
\end{cases}
$$

**Solution.**  
From (aₙ+1)(aₙ+2)≤0, one deduces −2≤aₙ≤−1. Induction confirms invariance of this interval. Then
$$
a_{n+1}-a_n=(a_n+1)(a_n+2)\le 0,
$$
so {aₙ} is decreasing and bounded. Therefore it converges to some ℓ.  
The fixed-point equation gives
$$
\ell=\ell^2+4\ell+2 \quad\Longrightarrow\quad \ell^2+3\ell+2=0 \quad\Rightarrow\quad \ell\in\{-2,-1\}.
$$
By monotonicity and the initial value a₁=−1.5, the limit is ℓ=−2.

**Final result**  
$$
\lim_{n\to\infty} a_n=-2.
$$

---

### Exercise 2
$$
\begin{cases}
a_1=2,\\
a_{n+1}=2\sqrt{a_n}.
\end{cases}
$$

**Solution.**  
If 0≤aₙ≤4 then a_{n+1}≥aₙ. By induction the sequence remains in [0,4] and is increasing.  
Thus it converges to some ℓ with
$$
\ell=2\sqrt{\ell}\quad\Longrightarrow\quad \ell(\ell-4)=0.
$$
Since a₁=2, the acceptable limit is ℓ=4.

**Final result**  
$$
\lim_{n\to\infty} a_n=4.
$$

---

### Exercise 3
$$
\begin{cases}
a_1=5,\\
a_{n+1}=\dfrac{a_n}{\tfrac12+a_n}.
\end{cases}
$$

**Solution.**  
For aₙ>0,
$$
\frac{a_n}{\tfrac12+a_n}\le a_n \iff a_n\ge\tfrac12.
$$
By induction aₙ≥1/2 for all n, so the sequence is decreasing and bounded below.  
Hence it converges to ℓ solving
$$
\ell=\frac{\ell}{\tfrac12+\ell} \quad\Longrightarrow\quad \ell(\ell-\tfrac12)=0.
$$
The only acceptable solution is ℓ=1/2.

**Final result**  
$$
\lim_{n\to\infty} a_n=\tfrac12.
$$

---

### Exercise 4
$$
\begin{cases}
a_1=\tfrac12,\\
a_{n+1}=a_n^{3}.
\end{cases}
$$

**Solution.**  
By induction 0≤aₙ≤1. Then a_{n+1}=a_n³≤a_n, so {aₙ} is decreasing and bounded. It converges to ℓ satisfying
$$
\ell=\ell^{3}.
$$
Thus ℓ∈{−1,0,1}. By bounds, only ℓ=0 is possible.

**Final result**  
$$
\lim_{n\to\infty} a_n=0.
$$

---

### Exercise 5 (parameter a>0)
$$
\begin{cases}
a_1=a,\\
a_{n+1}=\tfrac12(a+a_n^{2}).
\end{cases}
$$

**Solution.**  
If 0<a≤1, the inequalities
$$
1-\sqrt{1-a}\le a_n \le 1+\sqrt{1-a}
$$
define an invariant interval, inside which {aₙ} is decreasing.  
Thus it converges to a fixed point:
$$
\ell=\tfrac12(a+\ell^2) \quad\Rightarrow\quad \ell=1\pm\sqrt{1-a}.
$$
Monotonicity selects ℓ=1−√(1−a).  
If a=1, the sequence is constant (aₙ=1).  
If a>1, the recursion pushes upwards and diverges.

**Final result**  
$$
\lim_{n\to\infty} a_n=
\begin{cases}
1-\sqrt{1-a}, & 0<a\le1,\\
1, & a=1,\\
+\infty, & a>1.
\end{cases}
$$

---

### Exercise 6
$$
\begin{cases}
a_1=\tfrac32,\\
a_{n+1}=\tfrac{a_n}{2}+\tfrac{1}{a_n}.
\end{cases}
$$

**Solution.**  
For aₙ>0,
$$
a_{n+1}-\sqrt{2}=\frac{(a_n-\sqrt{2})^2}{2a_n}\ge0.
$$
Thus aₙ≥√2 and the recursion implies a_{n+1}≤aₙ.  
So {aₙ} is decreasing, bounded below, and convergent.  
Fixed point:
$$
\ell=\tfrac{\ell}{2}+\tfrac{1}{\ell}\quad\Longrightarrow\quad \ell^2=2.
$$
Since aₙ>0, ℓ=√2.

**Final result**  
$$
\lim_{n\to\infty} a_n=\sqrt{2}.
$$

---

### Exercise 7 (parameter α>0)
$$
\begin{cases}
a_0=\alpha,\\
a_{n+1}=a_n^{2}-a_n+1.
\end{cases}
$$

**Solution.**  
Since a_{n+1}−a_n=(a_n−1)²≥0, the sequence is increasing.  
If it converged, then
$$
\ell=\ell^2-\ell+1 \quad\Rightarrow\quad (\ell-1)^2=0 \quad\Rightarrow\quad \ell=1.
$$
Thus:
- if 0<α≤1, bounded increasing ⇒ ℓ=1;  
- if α>1, increasing and surpasses fixed point ⇒ diverges.

**Final result**  
$$
\lim_{n\to\infty} a_n=
\begin{cases}
1, & 0<\alpha\le1,\\
+\infty, & \alpha>1.
\end{cases}
$$

---

### Exercise 8
$$
\begin{cases}
a_1=\tfrac12,\\
a_{n+1}=\dfrac{1}{4-a_n}.
\end{cases}
$$

**Solution.**  
By induction 2−√3≤aₙ≤2+√3, ensuring denominators positive.  
The sequence is decreasing and bounded below, hence convergent.  
Fixed point:
$$
\ell=\frac{1}{4-\ell}\quad\Longrightarrow\quad \ell^2-4\ell+1=0.
$$
Solutions are ℓ=2±√3. Bounds select ℓ=2−√3.

**Final result**  
$$
\lim_{n\to\infty} a_n=2-\sqrt{3}.
$$

---

### Exercise 9
$$
\begin{cases}
a_1=4,\\
a_{n+1}=2\sqrt{a_n^{2}-6}.
\end{cases}
$$

**Solution.**  
For aₙ≥√6, recursion is defined. One shows aₙ≥2√2 and a_{n+1}≥a_n, so the sequence is monotone increasing.  
No finite fixed point is consistent with monotonicity, hence it diverges.

**Final result**  
$$
\lim_{n\to\infty} a_n=+\infty.
$$

---

### Exercise 10
$$
\begin{cases}
a_1=\tfrac{\pi}{2},\\
a_{n+1}=\sin a_n.
\end{cases}
$$

**Solution.**  
On [0,π/2], sin t≤t. By induction 0≤aₙ≤π/2 and {aₙ} is decreasing.  
Hence converges to ℓ with
$$
\ell=\sin \ell.
$$
The only fixed point is ℓ=0.

**Final result**  
$$
\lim_{n\to\infty} a_n=0.
$$

</div>

---

<div class="content-box">

## Explore more topics in Calculus 1

- [Complex Numbers](/university/math/calculus-1/complex-numbers/)  
- [Notable Limits](/university/math/calculus-1/notable-limits/)  
- [Limits with L’Hôpital’s Rule](/university/math/calculus-1/limits-hopital/)  
- [Limits with Taylor Expansions](/university/math/calculus-1/limits-taylor/)  
- [Sequences](/university/math/calculus-1/sequences/)  
- [Series](/university/math/calculus-1/series/)  
- [Continuity](/university/math/calculus-1/continuity/)  
- [Differentiability](/university/math/calculus-1/differentiability/)  
- [Integration by Parts](/university/math/calculus-1/integration-by-parts/)  
- [Integration by Substitution](/university/math/calculus-1/integration-substitution/)  
- [General ODEs](/university/math/calculus-1/odes-general/)  
- [Cauchy Problems for ODEs](/university/math/calculus-1/odes-cauchy/)  

</div>
