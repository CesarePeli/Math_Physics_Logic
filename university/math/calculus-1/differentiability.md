---
layout: default
date: 2025-08-29
title: "Solved Exercises — Differentiability"
meta-description: "Worked exercises on differentiability: functions defined by parts, conditions for differentiability, absolute value and radical functions, logarithmic-exponential forms, and smoothness classification."
permalink: "/university/math/calculus-1/differentiability/"
background_image: "/images/grafi.png"

---

<div class="content-box">

## Theoretical Recall

A function $f$ is **differentiable at $x_0$** if the limit

$$
f'(x_0) = \lim_{h \to 0} \frac{f(x_0+h)-f(x_0)}{h}
$$

exists and is finite. Differentiability implies continuity, but not vice versa.

- **Corners/cusps:** arise when one-sided derivatives differ or blow up.  
- **Vertical tangents:** derivative tends to $\pm\infty$.  
- **Piecewise definitions:** for differentiability at the junction, require both continuity and equality of left/right derivatives.  
- **Higher smoothness:** $C^k(\mathbb{R})$ denotes $k$-times continuously differentiable functions.  

</div>

<div class="content-box">

## Exercises

### Exercise 1
Verify continuity and differentiability of

$$
f(x)=
\begin{cases}
x^2, & x\ge 0, \\
-x, & x<0.
\end{cases}
$$

**Solution:**  
At $0$, $\lim_{x\to0^+}f(x)=0=\lim_{x\to0^-}f(x)=f(0)$.  
Left derivative: $\lim_{h\to0^-}\frac{f(h)-f(0)}{h}=\lim_{h\to0^-}\frac{-h}{h}=-1$.  
Right derivative: $\lim_{h\to0^+}\frac{h^2}{h}=0$.  
Since they differ, $f$ is continuous but not differentiable at $0$.

**Final Result:**

$$
f \in C^0(\mathbb{R}), \quad f \notin C^1(\mathbb{R}) \text{ (not differentiable at } 0).
$$

---

### Exercise 2
Study differentiability of $f(x)=x\sqrt{|x|}$.

**Solution:**  
For $x>0$: $f(x)=x^{3/2}$, $f'(x)=\tfrac{3}{2}\sqrt{x}$.  
For $x<0$: $f(x)=-x\sqrt{-x}=-(-x)^{3/2}$, $f'(x)=-\tfrac{3}{2}\sqrt{-x}$.  
At $0$: $\lim_{h\to0^+}\frac{h^{3/2}}{h}=\sqrt{h}\to0$,  
$\lim_{h\to0^-}\frac{-(-h)^{3/2}}{h}=\lim_{h\to0^+}\frac{h^{3/2}}{-h}=-\sqrt{h}\to0$.  
So $f'(0)=0$.  

**Final Result:**

$$
f \in C^1(\mathbb{R}).
$$

---

### Exercise 3
Consider $f(x)=|x|\sqrt{|x|}$. Study differentiability at $0$.

**Solution:**  
For $x>0$: $f(x)=x^{3/2}$, $f'(x)=\tfrac{3}{2}\sqrt{x}\to0$.  
For $x<0$: $f(x)=(-x)^{3/2}$, derivative $f'(x)=-\tfrac{3}{2}\sqrt{-x}\to0$.  
At $0$, both one-sided derivatives $=0$. Hence differentiable at $0$ with $f'(0)=0$.  

**Author’s note:** Although the function involves absolute values and radicals, the exponents $>1$ guarantee smoothness at the origin.

**Final Result:**

$$
f \in C^1(\mathbb{R}).
$$

---

### Exercise 4
Study differentiability of $f(x)=|x|\sqrt{1-x}$ at $x=1$.

**Solution:**  
For $x<1$, $f$ is defined and continuous. At $x=1$: $f(1)=0$.  
Right of 1 not in domain. Left derivative:  
$$
\lim_{h\to0^-}\frac{f(1+h)-0}{h}=\lim_{h\to0^-}\frac{|1+h|\sqrt{-h}}{h}.
$$
For $h\to0^-$, numerator $\sim \sqrt{-h}$, denominator $h<0$. Ratio $\to -\infty$.  

**Final Result:**

$$
f \text{ not differentiable at } 1 \text{ (vertical tangent)}.
$$

---

### Exercise 5
$f(x)=x^x\log x$ for $x>0$, extended by $f(0)=0$. Check differentiability at $0$.

**Solution:**  
For $x>0$, write $f(x)=e^{x\log x}\log x$. Expansion: $x\log x\to0^-$ as $x\to0^+$, so $x^x\to1$. Then $f(x)\sim \log x$.  
Thus $\lim_{x\to0^+}\frac{f(x)-0}{x}=\lim_{x\to0^+}\frac{\log x}{x}=-\infty$.  

**Final Result:**

$$
f \text{ is continuous at }0 \text{ but not differentiable (derivative } -\infty).
$$

---

### Exercise 6
$f(x)=
\begin{cases}
ax+b,& x<0, \\
x^2,& x\ge0.
\end{cases}$  
Find $a,b$ such that $f$ is differentiable at $0$.

**Solution:**  
Continuity: $\lim_{x\to0^-}(ax+b)=b=f(0)=0 \Rightarrow b=0$.  
Left derivative: $\lim_{h\to0^-}\frac{ah}{h}=a$.  
Right derivative: $\lim_{h\to0^+}\frac{h^2}{h}=0$.  
Equality $\Rightarrow a=0$.  

**Final Result:**

$$
a=0,\; b=0 \quad\Rightarrow f \in C^1(\mathbb{R}).
$$

---

### Exercise 7
For which $a\in\mathbb{R}$ is
$$
f(x)=|x|^a
$$
of class $C^k(\mathbb{R})$?

**Solution:**  
Near $0$:  
- If $a>k$, derivatives up to order $k$ exist and are continuous.  
- If $a$ not integer, differentiability breaks at some finite order.  

**Author’s note:** The function smoothness depends directly on the exponent.  

**Final Result:**

$$
f \in C^k(\mathbb{R}) \iff a>k.
$$

---

### Exercise 8
Find $a,b$ for which
$$
f(x)=
\begin{cases}
ax^2+bx,& x\ge0, \\
\sin x,& x<0
\end{cases}
$$
is continuous and differentiable at $0$.

**Solution:**  
Continuity at 0: $\lim_{x\to0^-}\sin x=0=f(0)\Rightarrow$ automatic.  
Derivative: left derivative $\cos 0=1$. Right derivative $\lim_{h\to0^+}\frac{ah^2+bh}{h}=b$.  
So require $b=1$. $a$ free.  

**Final Result:**

$$
b=1,\; a \text{ arbitrary}.
$$

---

### Exercise 9
Find $a,b$ so that
$$
f(x)=
\begin{cases}
ax+b,& x<0, \\
x^2,& x\ge0
\end{cases}
$$
is $C^1$ at $0$.

**Solution:**  
Continuity: $b=0$.  
Derivative: left derivative $=a$, right derivative $=0$. Require $a=0$.  

**Final Result:**

$$
a=0,\; b=0.
$$

---

### Exercise 10
Find $a,b,c$ so that
$$
f(x)=
\begin{cases}
ax^2+bx+c,& x<0, \\
\cos x,& x\ge0
\end{cases}
$$
is $C^2(\mathbb{R})$.

**Solution:**  
At $0$: $c=f(0)=\cos0=1$.  
Derivative: left $f'(0^-)=b$, right $f'(0^+)= -\sin 0=0$. So $b=0$.  
Second derivative: left $f''(0^-)=2a$, right $f''(0^+)= -\cos 0=-1$.  
So $2a=-1 \Rightarrow a=-\tfrac{1}{2}$.  

**Final Result:**

$$
a=-\tfrac{1}{2},\; b=0,\; c=1.
$$

</div>

<div class="content-box">

## Other Topics in Calculus I

- [Complex Numbers]({{ "/university/math/calculus-1/complex-numbers/" | relative_url }})
- [Notable Limits](/university/math/calculus-1/notable-limits/)  
- [Limits with L’Hôpital’s Rule](/university/math/calculus-1/limits-hopital/)  
- [Limits with Taylor Expansions](/university/math/calculus-1/limits-taylor/)  
- [Sequences](/university/math/calculus-1/sequences/)  
- [Series](/university/math/calculus-1/series/)  
- [Continuity](/university/math/calculus-1/continuity/)  
 
- [Integration by Parts](/university/math/calculus-1/integration-by-parts/)  
- [Integration by Substitution](/university/math/calculus-1/integration-substitution/)  
- [General ODEs](/university/math/calculus-1/odes-general/)  
- [Cauchy Problems for ODEs](/university/math/calculus-1/odes-cauchy/)  

These pages combine theoretical background and step-by-step worked examples.

</div>