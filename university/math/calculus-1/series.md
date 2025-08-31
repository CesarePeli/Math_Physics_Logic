---
layout: default
date: 2025-08-31
title: "Solved Exercises — Sequences and Series of Functions"
meta-description: "Uniform vs pointwise convergence, total convergence, power series radius and sums: 10 selected exercises with faithful solutions and author’s original remarks."
permalink: "/university/math/calculus-1/series/"
background_image: "/images/serie.png"
featured: false
---

<div class="content-box">

## Theoretical Recall

Let  

$$
A \subset \mathbb{R}, \qquad (f_n), \qquad f_n : A \to \mathbb{R}, \qquad f : A \to \mathbb{R}.
$$

---

### Pointwise convergence
The sequence \(f_n\) converges **pointwise** to \(f\) on \(A\) if  

$$
\lim_{n \to \infty} f_n(x) = f(x), \qquad \forall x \in A.
$$

Equivalently: for every \(\varepsilon > 0\), there exists \(n_{\varepsilon,x}\) such that for all \(n > n_{\varepsilon,x}\),  

$$
|f_n(x) - f(x)| < \varepsilon .
$$

---

### Uniform convergence
The sequence \(f_n\) converges **uniformly** to \(f\) on \(A\) if  

$$
\forall \varepsilon > 0,\ \exists n_\varepsilon :\ 
\forall n > n_\varepsilon,\ \forall x \in A,\quad |f_n(x)-f(x)| < \varepsilon .
$$

Equivalently, setting  

$$
\alpha_n = \sup_{x \in A} |f_n(x) - f(x)| ,
$$

we have  

$$
\alpha_n \to 0 .
$$

---

### Facts
- Uniform convergence \(\Rightarrow\) pointwise convergence (not conversely).  

- If \( f_n \rightrightarrows f \) and each \( f_n \) is continuous on an interval \( I \), then \( f \) is continuous on \( I \).  

- Limits commute with integrals:  

$$
\int_a^b f_n(x)\,dx \;\to\; \int_a^b f(x)\,dx .
$$

- If moreover  

$$
f_n \to f, \qquad f_n' \rightrightarrows g, \qquad f_n \in C^1(I),
$$  

then  

$$
f \in C^1(I), \qquad f' = g .
$$

</div>


<div class="content-box">

## Exercises

**Note.** When summing a power series, unless otherwise specified, sums are understood on intervals  
$$
[x_0 - \rho,\, x_0 + \rho], \quad 0 \leq \rho \leq r
$$  
where \(r\) is the radius of convergence.

---

**Ex 1.** For \(x \in [0,1]\) and \(p \in \mathbb{R}\), consider  

$$
f_n(x) = n^{p}\,x\,e^{-n x^{2}} .
$$  

Study pointwise and uniform convergence (as \(p\) varies).

**Solution:**  
By comparison of infinitesimals,  

$$
\lim_{n\to\infty} f_n(x) = 0 \quad \forall x \in [0,1],
$$  

so \( f_n \to 0 \) pointwise.  

For uniform convergence (the functions are continuous), compute the maximum:  

$$
f_n'(x) = n^{p} e^{-n x^{2}} (1 - 2n x^{2}).
$$  

The maximum occurs at  

$$
x = \frac{1}{\sqrt{2n}} ,
$$  

hence  

$$
\alpha_n = \sup_{x \in [0,1]} |f_n(x)| 
= \frac{e^{-1/2}}{\sqrt{2}} \, n^{\,p-\tfrac12}.
$$  

Therefore  

$$
\lim_{n \to \infty} \alpha_n =
\begin{cases}
0 & p < \tfrac12, \\[6pt]
\dfrac{e^{-1/2}}{\sqrt{2}} & p = \tfrac12, \\[6pt]
+\infty & p > \tfrac12 .
\end{cases}
$$  

**Observation:** The exponential decay dominates only if \(p < \tfrac12\).  

**Final Result:**  

$$
\text{Pointwise: } f_n \to 0. 
\quad \text{Uniform on } [0,1] \ \text{iff } p < \tfrac12 .
$$

---

**Ex 2.** For \(x \ge 0\),  

$$
f_n(x) = \sqrt[n]{\,n + x^{n}\,} .
$$  

Study pointwise and uniform convergence.

**Solution:**  
Pointwise limit:  

$$
\lim_{n\to\infty} f_n(x) =
\begin{cases}
1 & x \in [0,1], \\[6pt]
x & x > 1 .
\end{cases}
$$  

For uniform convergence on \([0,\infty)\):  

- On \([0,1]\):  

$$
\alpha_{n,1} = \sup_{x\in[0,1]} |f_n(x)-1| 
= \sqrt[n]{n+1}-1 \to 0 .
$$  

- On \([1,\infty)\):  

$$
g_n(x) = (n+x^n)^{1/n} - x, \qquad 
g_n'(x) = \left(\tfrac{n}{x^{n}}+1\right)^{\frac{1-n}{n}} - 1 < 0.
$$  

So \(g_n\) is decreasing and  

$$
\alpha_{n,2} = \sup_{x\in[1,\infty)} |f_n(x)-x|
= \sqrt[n]{n+1}-1 \to 0 .
$$  

Thus  

$$
\alpha_n = \sup_{x\in[0,\infty)} |f_n(x)-f(x)| \to 0 .
$$  

**Observation:** Uniform convergence holds globally, even though the pointwise limit function changes definition at \(x=1\).  

**Final Result:**  

$$
\text{Pointwise: } f_n \to f,\ 
f(x) = \begin{cases} 1 & x \in [0,1], \\ x & x > 1. \end{cases} 
\quad \text{Uniform on } [0,\infty) .
$$

---

**Ex 3.** For \(x \in [0,1]\),  

$$
f_n(x) = n^{2} x^{n} (1-x^{4}) .
$$  

**Solution:**  
Clearly  

$$
f_n(x) \to 0 \quad \forall x \in [0,1].
$$  

For uniform convergence,  

$$
f_n'(x) = n^{2} x^{n-1} \bigl( n - (n+4)x^{4} \bigr).
$$  

The maximum is at  

$$
x = \left(\frac{n}{n+4}\right)^{1/4},
$$  

hence  

$$
\alpha_n = n^{2} \left( \frac{n}{n+4} \right)^{n/4} \frac{4}{n+4}
\;\to\; +\infty .
$$  

**Observation:** The growth of \(n^2\) prevents uniform convergence despite pointwise vanishing.  

**Final Result:**  

$$
\text{Pointwise: } f_n \to 0, 
\qquad \text{Not uniform on } [0,1].
$$

---

**Ex 4.** For \(x \in [0,1]\) and \(p \in \mathbb{R}\),  

$$
f_n(x) = n^{p} x^{n} (1-x^{2}) .
$$  

**Solution:**  
Pointwise,  

$$
f_n(x) \to 0 .
$$  

Derivative:  

$$
f_n'(x) = n^{p} x^{n-1} \bigl( n - (n+2)x^{2} \bigr).
$$  

Maximum at  

$$
x = \sqrt{\tfrac{n}{n+2}} .
$$  

So  

$$
\alpha_n = n^{p} \left(\frac{n}{n+2}\right)^{n/2} \frac{2}{n+2}.
$$  

Hence  

$$
\alpha_n \to
\begin{cases}
0 & p < 1, \\[6pt]
\dfrac{2}{e} & p = 1, \\[6pt]
+\infty & p > 1 .
\end{cases}
$$  

**Observation:** The balance between polynomial growth and exponential decay breaks precisely at \(p=1\).  

**Final Result:**  

$$
\text{Pointwise: } f_n \to 0, 
\qquad \text{Uniform on } [0,1] \ \text{iff } p < 1 .
$$

---

**Ex 5.** For \(x \in [0,1]\),  

$$
f_n(x) = \frac{\sin(nx)}{n} .
$$  

**Solution:**  
By notable limits,  

$$
\lim_{n\to\infty} f_n(x) = 0 ,
$$  

so pointwise convergence holds.  

Since  

$$
|f_n(x)| \le \frac{1}{n},
$$  

we have  

$$
\alpha_n \le \frac{1}{n} \to 0 .
$$  

**Observation:** The sine oscillation, bounded by \(1\), ensures uniform convergence at the same rate as \(1/n\).  

**Final Result:**  

$$
\text{Pointwise: } f_n \to 0, 
\qquad \text{Uniform on } [0,1].
$$

---

**Ex 6.** For \(x \in \mathbb{R}\),  

$$
f_n(x) = \arctan(nx) .
$$  

**Solution:**  
Pointwise limit:  

$$
\lim_{n\to\infty} f_n(x) =
\begin{cases}
\frac{\pi}{2} & x > 0, \\[6pt]
0 & x = 0, \\[6pt]
-\frac{\pi}{2} & x < 0 .
\end{cases}
$$  

No uniform convergence on \(\mathbb{R}\) since the limit is discontinuous.  

For any \(a > 0\):  

$$
\sup_{x \le -a} \left| f_n(x) + \frac{\pi}{2} \right|
= \frac{\pi}{2} - \arctan(na) \to 0 ,
$$  

$$
\sup_{x \ge a} \left| f_n(x) - \frac{\pi}{2} \right|
= \frac{\pi}{2} - \arctan(na) \to 0 .
$$  

**Observation:** Uniform convergence holds only away from the discontinuity at \(x=0\).  

**Final Result:**  

$$
\text{No uniform convergence on } \mathbb{R}, 
\quad \text{Uniform on } [a,\infty),\ (-\infty,-a] \ \forall a>0 .
$$

---

**Ex 7.** Study convergence and compute the sum of  

$$
\sum_{n=1}^{\infty}\frac{n+1}{n!}\,x^{n},\qquad x\in\mathbb{R}.
$$  

**Solution:**  
Ratio test:  

$$
r = \infty ,
$$  

so absolute convergence for all \(x\).  

Split:  

$$
\sum_{n=1}^\infty \frac{n}{n!} x^{n}
= x \sum_{n=1}^\infty \frac{x^{n-1}}{(n-1)!}
= x e^{x},
$$  

$$
\sum_{n=1}^\infty \frac{x^{n}}{n!} = e^{x} - 1 .
$$  

Thus  

$$
s(x) = x e^{x} + e^{x} - 1 .
$$  

**Observation:** The manipulation uses termwise differentiation/integration of power series.  

**Final Result:**  

$$
\sum_{n=1}^{\infty}\frac{n+1}{n!}\,x^{n} 
= e^{x}(1+x) - 1 .
$$

---

**Ex 8.** Study the series  

$$
\sum_{n=1}^{\infty}(2^{n}+3^{n})\,x^{n}.
$$  

**Solution:**  
Ratio test:  

$$
\lim_{n\to\infty}\frac{a_{n+1}}{a_n} = 3,
\qquad r = \tfrac13.
$$  

At \(x=\tfrac13\):  

$$
\sum \frac{2^{n}+3^{n}}{3^{n}}
$$  

diverges.  

At \(x=-\tfrac13\):  

$$
\sum \frac{2^{n}+3^{n}}{3^{n}}(-1)^{n}
$$  

does not converge.  

**Observation:** Even if the radius is finite, both endpoints fail here.  

**Final Result:**  

$$
\text{Convergence set } X = \Bigl(-\tfrac{1}{3},\tfrac{1}{3}\Bigr).
$$

---

**Ex 9.** Study and sum  

$$
\sum_{n=1}^{\infty}(-1)^{n}\,n\,x^{2n-1}.
$$  

**Solution:**  
Root test:  

$$
r = 1, \qquad X = (-1,1).
$$  

For \(|x|<1\):  

$$
\sum_{n=1}^{\infty}(-1)^{n} n x^{2n-1}
= D\!\left[\sum_{n=1}^{\infty}\frac{(-1)^{n}}{2}x^{2n}\right]
= D\!\left[\frac{1}{2(1+x^{2})}\right]
= -\frac{x}{(1+x^{2})^{2}} .
$$  

**Observation:** Differentiating a simple geometric series is the key step.  

**Final Result:**  

$$
\sum_{n=1}^{\infty}(-1)^{n}n x^{2n-1}
= -\frac{x}{(1+x^{2})^{2}},\qquad |x|<1 .
$$

---

**Ex 10.** Study and sum  

$$
\sum_{n=0}^{\infty}\frac{x^{n}}{(n+1)(n+2)}.
$$  

**Solution:**  
Root test:  

$$
r = 1, \qquad X = [-1,1].
$$  

Use double integration:  

$$
\sum_{n=0}^{\infty}\frac{x^{n}}{(n+1)(n+2)}
= \frac{1}{x^{2}}\int_{0}^{x}\int_{0}^{y}\sum_{n=0}^{\infty}t^{n}\,dt\,dy
= \frac{1}{x^{2}}\int_{0}^{x}\int_{0}^{y}\frac{1}{1-t}\,dt\,dy
= \frac{(1-x)\log(1-x)}{x^{2}} + \frac{1}{x}.
$$  

**Observation:** Double integration allows to reduce the denominator \((n+1)(n+2)\).  

**Final Result:**  

$$
\sum_{n=0}^{\infty}\frac{x^{n}}{(n+1)(n+2)}
= \frac{(1-x)\,\log(1-x)}{x^{2}} + \frac{1}{x}.
$$

</div>


---


<div class="content-box">

## Explore more topics in Calculus 1

- [Complex Numbers]({{ "/university/math/calculus-1/complex-numbers/" | relative_url }})  
- [Notable Limits](/university/math/calculus-1/notable-limits/)  
- [Limits with L’Hôpital’s Rule](/university/math/calculus-1/limits-hopital/)  
- [Limits with Taylor Expansions](/university/math/calculus-1/limits-taylor/)  
- [Sequences](/university/math/calculus-1/sequences/)  
- [Continuity](/university/math/calculus-1/continuity/)  
- [Differentiability](/university/math/calculus-1/differentiability/)  
- [Integration by Parts](/university/math/calculus-1/integration-by-parts/)  
- [Integration by Substitution](/university/math/calculus-1/integration-substitution/)  
- [General ODEs](/university/math/calculus-1/odes-general/)  
- [Cauchy Problems for ODEs](/university/math/calculus-1/odes-cauchy/)  

</div>
