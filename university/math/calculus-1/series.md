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

**Note.** When summing a power series, unless otherwise specified, sums are understood on intervals $[x_0-\rho,\,x_0+\rho]$ with $0\le \rho\le r$ (where $r$ is the radius of convergence).

---

**Ex 1.** For $x\in[0,1]$ and $p\in\mathbb{R}$, consider
$$
f_n(x)=n^{p}\,x\,e^{-n x^{2}}.
$$
Study pointwise and uniform convergence (as $p$ varies).

**Solution:**  
By comparison of infinitesimals, $\lim_{n\to\infty} f_n(x)=0$ for each $x\in[0,1]$, so $f_n\to 0$ pointwise. For uniform convergence (the functions are continuous), find the maximum:
$$
f_n'(x)=n^{p}e^{-n x^{2}}(1-2n x^{2}).
$$
The maximum occurs at $x=\tfrac{1}{\sqrt{2n}}$, hence
$$
\alpha_n=\sup_{x\in[0,1]}|f_n(x)|=\frac{e^{-1/2}}{\sqrt{2}}\,n^{\,p-\frac12},
$$
so
$$
\lim_{n\to\infty}\alpha_n=
\begin{cases}
0 & p<\tfrac12,\\[2pt]
\dfrac{e^{-1/2}}{\sqrt{2}} & p=\tfrac12,\\[6pt]
+\infty & p>\tfrac12.
\end{cases}
$$

**Final Result:**  
$$
\text{Pointwise: } f_n\to0.\quad \text{Uniform on }[0,1]\ \text{iff }p<\tfrac12.
$$

---

**Ex 2.** For $x\ge0$,
$$
f_n(x)=\sqrt[n]{\,n+x^{n}\,}.
$$
Study pointwise and uniform convergence.

**Solution:**  
Pointwise,
$$
\lim_{n\to\infty}f_n(x)=
\begin{cases}
1,& x\in[0,1],\\
x,& x>1.
\end{cases}
$$
For uniform convergence on $[0,\infty)$ split:

- On $[0,1]$, $f_n(x)-1$ is increasing, so
$\alpha_{n,1}=\sup_{[0,1]}|f_n-1|=\sqrt[n]{n+1}-1\to0$.

- On $[1,\infty)$, with $g_n(x)=(n+x^n)^{1/n}-x$,
$$
g_n'(x)=\Bigl(\tfrac{n}{x^{n}}+1\Bigr)^{\!\frac{1-n}{n}}-1<0,
$$
so $g_n$ is decreasing and
$\alpha_{n,2}=\sup_{[1,\infty)}|f_n-x|=\sqrt[n]{n+1}-1\to0$.

Thus $\alpha_n=\sup_{[0,\infty)}|f_n-f|\to0$.

**Final Result:**  
$$
\text{Pointwise: } f_n\to f,\ f(x)=\begin{cases}1,&x\in[0,1],\\ x,&x>1.\end{cases}
\quad \text{Uniform on }[0,\infty).
$$

---

**Ex 3.** For $x\in[0,1]$,
$$
f_n(x)=n^{2}x^{n}(1-x^{4}).
$$
Study pointwise and uniform convergence.

**Solution:**  
Clearly $f_n(x)\to0$ pointwise. For uniformity, maximize:
$$
f_n'(x)=n^{2}x^{n-1}[n-(n+4)x^{4}],
$$
with maximizer $x=\bigl(\tfrac{n}{n+4}\bigr)^{1/4}$. Then
$$
\alpha_n=n^{2}\Bigl(\frac{n}{n+4}\Bigr)^{\!n/4}\frac{4}{n+4}\to+\infty,
$$
hence no uniform convergence.

**Final Result:**  
$$
\text{Pointwise: } f_n\to0,\qquad \text{not uniform on }[0,1].
$$

---

**Ex 4.** For $x\in[0,1]$ and $p\in\mathbb{R}$,
$$
f_n(x)=n^{p}x^{n}(1-x^{2}).
$$
Study pointwise and uniform convergence as $p$ varies.

**Solution:**  
Pointwise $f_n(x)\to0$. For uniformity:
$$
f_n'(x)=n^{p}x^{n-1}[\,n-(n+2)x^{2}\,],
$$
maximum at $x=\sqrt{n/(n+2)}$, hence
$$
\alpha_n=n^{p}\Bigl(\frac{n}{n+2}\Bigr)^{\!n/2}\frac{2}{n+2}\ \xrightarrow[n\to\infty]{}\ 
\begin{cases}
0,& p<1,\\[2pt]
\dfrac{2}{e},& p=1,\\[4pt]
+\infty,& p>1.
\end{cases}
$$

**Final Result:**  
$$
\text{Pointwise: } f_n\to0,\qquad \text{uniform on }[0,1]\ \text{iff }p<1.
$$

---

**Ex 5.** For $x\in[0,1]$,
$$
f_n(x)=\frac{\sin(nx)}{n}.
$$
Study the behavior.

**Solution:**  
Using notable limits, $\lim_{n\to\infty}f_n(x)=0$ pointwise. For uniform convergence:
$$
f_n'(x)=\cos(nx),
$$
and the (claimed) point of maximum is $x=n\pi$. Thus
$$
\alpha_n=\frac{\sin(n^{2}\pi)}{n}\to0,
$$
hence uniform convergence.

**Final Result:**  
$$
\text{Pointwise: } f_n\to0,\qquad \text{uniform on }[0,1].
$$

---

**Ex 6.** For $x\in\mathbb{R}$,
$$
f_n(x)=\arctan(nx).
$$
Study the behavior and uniform convergence on subsets.

**Solution:**  
Pointwise,
$$
\lim_{n\to\infty}f_n(x)=
\begin{cases}
\frac{\pi}{2},& x>0,\\[2pt]
0,& x=0,\\[2pt]
-\frac{\pi}{2},& x<0.
\end{cases}
$$
Since $f_n$ are continuous and the limit is discontinuous, there is no uniform convergence on $\mathbb{R}$. The functions are odd and increasing:
$$
f_n'(x)=\frac{n}{1+n^{2}x^{2}}>0.
$$
For any $a>0$,
$$
\sup_{x\le -a}\Bigl|f_n(x)+\frac{\pi}{2}\Bigr|=\frac{\pi}{2}-\arctan(na)\to0,\quad
\sup_{x\ge a}\Bigl|f_n(x)-\frac{\pi}{2}\Bigr|=\frac{\pi}{2}-\arctan(na)\to0.
$$

**Final Result:**  
$$
\text{No uniform convergence on }\mathbb{R},\ \text{but uniform on }[a,\infty)\ \text{and }(-\infty,-a]\ \forall a>0.
$$

---

**Ex 7.** Study convergence and compute the sum of
$$
\sum_{n=1}^{\infty}\frac{n+1}{n!}\,x^{n},\qquad x\in\mathbb{R}.
$$

**Solution:**  
Ratio test gives radius $r=\infty$; absolute (and total on $[-p,p]$) convergence for all $x$. Split:
$$
\sum_{n=1}^\infty \frac{n}{n!}x^{n}=x\sum_{n=1}^\infty\frac{x^{n-1}}{(n-1)!}=xe^{x},\qquad
\sum_{n=1}^\infty \frac{x^{n}}{n!}=e^{x}-1.
$$
Thus $s(x)=xe^{x}+e^{x}-1$. Alternatively, integrate termwise and differentiate back.

**Final Result:**  
$$
\sum_{n=1}^{\infty}\frac{(n+1)}{n!}\,x^{n}=e^{x}(1+x)-1.
$$

---

**Ex 8.** Study the power series
$$
\sum_{n=1}^{\infty}\bigl(2^{n}+3^{n}\bigr)\,x^{n}.
$$

**Solution:**  
By ratio, $\lim\frac{a_{n+1}}{a_n}=3$, so $r=\tfrac13$.  
At $x=\tfrac13$, $\sum \frac{2^{n}+3^{n}}{3^{n}}$ fails the necessary condition.  
At $x=-\tfrac13$, $\sum \frac{2^{n}+3^{n}}{3^{n}}(-1)^{n}$ does not converge by Leibniz here (as stated in the source).

**Final Result:**  
$$
\text{Convergence set }X=\Bigl(-\tfrac13,\tfrac13\Bigr).
$$

---

**Ex 9.** Study and sum
$$
\sum_{n=1}^{\infty}(-1)^{n}\,n\,x^{2n-1}.
$$

**Solution:**  
Root test yields radius $1$; $X=(-1,1)$. For $|x|<1$,
\[
\sum_{n=1}^{\infty}(-1)^{n}n x^{2n-1}
= D\!\left[\sum_{n=1}^{\infty}\frac{(-1)^{n}}{2}x^{2n}\right]
= D\!\left[\frac12\sum_{n=0}^{\infty}(-x^{2})^{n}\right]
= D\!\left[\frac{1}{2(1+x^{2})}\right]
= -\frac{x}{(1+x^{2})^{2}}.
\]

**Final Result:**  
$$
\sum_{n=1}^{\infty}(-1)^{n}n x^{2n-1}=-\dfrac{x}{(1+x^{2})^{2}},\qquad |x|<1.
$$

---

**Ex 10.** Study and sum
$$
\sum_{n=0}^{\infty}\frac{x^{n}}{(n+1)(n+2)}.
$$

**Solution:**  
Root test gives radius $1$ and (per source) $X=[-1,1]$. For the sum, use double integration:
\[
\sum_{n=0}^{\infty}\frac{x^{n}}{(n+1)(n+2)}
=\frac{1}{x^{2}}\int_{0}^{x}\int_{0}^{y}\sum_{n=0}^{\infty}t^{n}\,dt\,dy
=\frac{1}{x^{2}}\int_{0}^{x}\int_{0}^{y}\frac{1}{1-t}\,dt\,dy
= \frac{(1-x)\log(1-x)}{x^{2}}+\frac{1}{x}.
\]

**Final Result:**  
$$
\sum_{n=0}^{\infty}\frac{x^{n}}{(n+1)(n+2)}=\frac{(1-x)\,\log(1-x)}{x^{2}}+\frac{1}{x}.
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
