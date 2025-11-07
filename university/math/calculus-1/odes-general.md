---
layout: default
date: 2025-08-31
title: "Solved Exercises — Ordinary Differential Equations"
meta-description: "Ten worked ODEs (no Cauchy problems): separable equations, linear constant-coefficient equations, undetermined coefficients, and variation of parameters. Clear steps and final answers isolated."
permalink: "/university/math/calculus-1/odes-general/"
background_image: "/images/grafi.png"
featured: true
---

<div class="content-box">



## Theoretical Recall

> *“The universe is a differential equation.”* — H. Poincaré  

Differential equations are a fundamental tool to model real phenomena.  
A simple example is **Malthus’ model**: suppose the birth–death rate per unit time is constant.  
If a population at $t_0$ has size $x_0$, its growth is modeled by the Cauchy problem

$$
\begin{cases}
y'(t)=a y(t)\\[6pt]
y(t_0)=x_0
\end{cases}
$$

with $a \in \mathbb{R}$.  
The solution is

$$
y(t)=x_0 e^{a(t-t_0)}.
$$

For $a=0.02$, this model matches the growth of the human population between 1700 and 1961.

---

### Linear first-order ODEs

A linear first-order equation has the form

$$
y'(t)+a(t)\,y(t)=g(t),
$$

with $a(t),g(t)$ continuous.  
The general solution is

$$
y(t)=e^{-A(t)}\Biggl(c+\int g(t)\,e^{A(t)}\,dt\Biggr),
$$

where $c \in \mathbb{R}$ and

$$
A(t)=\int a(t)\,dt.
$$

For a Cauchy problem

$$
\begin{cases}
y'(t)+a(t)\,y(t)=g(t)\\[6pt]
y(t_0)=y_0
\end{cases}
$$

the solution becomes

$$
y(t)=e^{-A(t)}\Biggl(y_0+\int_{t_0}^{t} g(s)\,e^{A(s)}\,ds\Biggr),
\qquad
A(t)=\int_{t_0}^{t} a(s)\,ds.
$$

---

### Linear ODEs of order $k$ with constant coefficients

Consider the homogeneous equation

$$
y^{(k)}(t)+a_{k-1}y^{(k-1)}(t)+\dots+a_1 y'(t)+a_0 y(t)=0.
$$

Its characteristic polynomial is

$$
P(\lambda)=\lambda^k+a_{k-1}\lambda^{k-1}+\dots+a_1\lambda+a_0.
$$

If $\lambda_j$ is a real root with multiplicity $m_j$, then the fundamental solutions include

$$
e^{\lambda_j t},\ t e^{\lambda_j t},\ \dots,\ t^{m_j-1}e^{\lambda_j t}.
$$

If $\lambda_j=\sigma+i p$ and $\bar{\lambda_j}=\sigma-i p$ are complex conjugate roots of multiplicity $m_j$, the real fundamental set includes

$$
e^{\sigma t}\cos(pt),\ t e^{\sigma t}\cos(pt),\ \dots,\ t^{m_j-1}e^{\sigma t}\cos(pt),
$$

$$
e^{\sigma t}\sin(pt),\ t e^{\sigma t}\sin(pt),\ \dots,\ t^{m_j-1}e^{\sigma t}\sin(pt).
$$

---

### Non-homogeneous linear ODEs

Equations of the form

$$
y^{(k)}(t)+a_{k-1}y^{(k-1)}(t)+\dots+a_1 y'(t)+a_0 y(t)=g(t)
$$

can be solved by two main methods: **method of undetermined coefficients (similarity)** and **variation of parameters**.

#### Method of similarity
1. If $g(t)$ is a polynomial of degree $m$:
   - If $P(0)\neq 0$: try $y_p(t)=A_0+A_1 t+\dots+A_m t^m$.
   - If $P(0)=0$ with multiplicity $h$: try $y_p(t)=t^h(A_0+A_1 t+\dots+A_m t^m)$.

2. If $g(t)=p(t)e^{\lambda t}$ with $p(t)$ polynomial of degree $m$:
   - If $P(\lambda)\neq 0$: try $y_p(t)=(A_0+A_1 t+\dots+A_m t^m)e^{\lambda t}$.
   - If $P(\lambda)=0$ with multiplicity $h$: try $y_p(t)=t^h(A_0+A_1 t+\dots+A_m t^m)e^{\lambda t}$.

3. If $g(t)=\alpha\cos(\lambda t)+\beta\sin(\lambda t)$:
   - If $P(i\lambda)\neq 0$: try $y_p(t)=A\cos(\lambda t)+B\sin(\lambda t)$.
   - If $P(i\lambda)=0$ with multiplicity $h$: try $y_p(t)=t^h(A\cos(\lambda t)+B\sin(\lambda t))$.

4. If $g(t)=e^{\mu t}(\alpha\cos(\lambda t)+\beta\sin(\lambda t))$:
   - If $P(\mu+i\lambda)\neq 0$: try $y_p(t)=e^{\mu t}(A\cos(\lambda t)+B\sin(\lambda t))$.
   - If $P(\mu+i\lambda)=0$ with multiplicity $h$: try $y_p(t)=t^h e^{\mu t}(A\cos(\lambda t)+B\sin(\lambda t))$.

5. If $g(t)=g_1(t)+g_2(t)$, solve separately for each part and sum the particular solutions.

#### Variation of parameters
Consider a second-order linear equation

$$
y''(x)+a(x)y'(x)+b(x)y(x)=f(x),
$$

with $a,b,f$ continuous.  
Let $y_1,y_2$ be two linearly independent solutions of the homogeneous equation.  
Define $z_1,z_2$ such that their derivatives solve

$$
\begin{cases}
z_1'(x)y_1(x)+z_2'(x)y_2(x)=0,\\[6pt]
z_1'(x)y_1'(x)+z_2'(x)y_2'(x)=f(x).
\end{cases}
$$

Then a particular solution is

$$
y_p(x)=z_1(x)y_1(x)+z_2(x)y_2(x).
$$



</div>

<div class="content-box">

## Exercises

> **Scope note.** This page **excludes Cauchy problems** (initial-value problems). Those will appear in a dedicated file.

---

### Exercise 1
$$
y'''(x)+3y''(x)=9x.
$$

**Solution.** Homogeneous part: $P(\lambda)=\lambda^2(\lambda+3)$,
$$
y_h=c_1+c_2x+c_3e^{-3x}.
$$
Right-hand side is polynomial; $P(0)=0$ with multiplicity 2 ⇒ try $y_p=x^2(Ax+B)$. Substituting gives $6A+18Ax+6B=9x$, hence $A=\tfrac12$, $B=-\tfrac12$ and
$$
y_p=\tfrac12x^3-\tfrac12x^2.
$$

**Final Result**
$$
y(x)=c_1+c_2x+c_3e^{-3x}+\tfrac12x^3-\tfrac12x^2.
$$

---

### Exercise 2
$$
y'''(x)+y(x)=x\,e^{-x}.
$$

**Solution.** $P(\lambda)=\lambda^3+1=(\lambda+1)(\lambda^2-\lambda+1)$, so
$$
y_h=c_1e^{-x}+c_2e^{x/2}\cos\!\left(\tfrac{\sqrt3}{2}x\right)+c_3e^{x/2}\sin\!\left(\tfrac{\sqrt3}{2}x\right).
$$
Forcing $x e^{-x}$ resonates at $\lambda=-1$ (simple root) ⇒ try $y_p=x(Ax+B)e^{-x}$. Substitution yields $A=\tfrac16$, $B=\tfrac13$, hence
$$
y_p=x\!\left(\tfrac16x+\tfrac13\right)e^{-x}.
$$

**Final Result**
$$
y(x)=c_1e^{-x}+c_2e^{x/2}\cos\!\left(\tfrac{\sqrt3}{2}x\right)+c_3e^{x/2}\sin\!\left(\tfrac{\sqrt3}{2}x\right)+x\!\left(\tfrac16x+\tfrac13\right)e^{-x}.
$$

---

### Exercise 3
$$
2y''(x)-5y'(x)+3y(x)=\sin(2x).
$$

**Solution.** $P(\lambda)=2\lambda^2-5\lambda+3$ ⇒ roots $1$ and $3/2$,
$$
y_h=c_1e^x+c_2e^{\frac32x}.
$$
No resonance at $2i$ ⇒ try $y_p=A\cos2x+B\sin2x$. Substituting gives
$$
\begin{cases}
10A-5B=1,\\
5A+10B=0,
\end{cases}
\quad\Rightarrow\quad A=\tfrac{2}{25},\ B=-\tfrac{1}{25}.
$$

**Final Result**
$$
y(x)=c_1e^x+c_2e^{\frac32x}+\tfrac{2}{25}\cos2x-\tfrac{1}{25}\sin2x.
$$

---

### Exercise 4
$$
y''(x)-2y'(x)+2y(x)=e^x+x\cos x.
$$

**Solution.** $P(\lambda)=\lambda^2-2\lambda+2$ ⇒ complex roots $1\pm i$,
$$
y_h=c_1e^x\cos x+c_2e^x\sin x.
$$
Split the forcing.

1) For $e^x$, $P(1)\neq0$ ⇒ try $y_{p1}=Ae^x$ ⇒ $A=1$.

2) For $x\cos x$, $P(i)\neq0$ ⇒ try $y_{p2}=(Bx+C)\cos x+(Dx+E)\sin x$. Solving the linear system yields
$$
B=\tfrac15,\quad C=\tfrac{2}{25},\quad D=-\tfrac{2}{5},\quad E=-\tfrac{14}{25}.
$$
Thus
$$
y_{p2}=\tfrac15\!\left[\left(x+\tfrac{2}{5}\right)\cos x-\left(2x+\tfrac{14}{5}\right)\sin x\right].
$$

**Final Result**
$$
y(x)=c_1e^x\cos x+c_2e^x\sin x+e^x+\tfrac15\!\left[\left(x+\tfrac{2}{5}\right)\cos x-\left(2x+\tfrac{14}{5}\right)\sin x\right].
$$

---

### Exercise 5
$$
y'(x)=e^{x+y(x)}.
$$

**Solution.** Separable:
$$
e^{-y}y'=e^x \quad\Rightarrow\quad \int e^{-y}\,dy=\int e^x\,dx
\quad\Rightarrow\quad -e^{-y}=e^x+C.
$$
Take $C=c_1>0$ to keep the log neat:
$$
e^{-y}=c_1-e^x,\qquad y(x)=-\log\!\bigl(c_1-e^x\bigr),
$$
with domain $x<\log c_1$.

**Final Result**
$$
y(x)=-\log\!\bigl(c_1-e^x\bigr),\qquad x<\log c_1.
$$

---

### Exercise 6
$$
y'''(x)-y''(x)-y'(x)+y(x)=e^x.
$$

**Solution.** $P(\lambda)=\lambda^3-\lambda^2-\lambda+1=(\lambda-1)^2(\lambda+1)$,
$$
y_h=c_1e^{-x}+c_2e^x+c_3xe^x.
$$
Forcing $e^x$ resonates with multiplicity 2 ⇒ try $y_p=A x^2 e^x$. Substitution gives $4A=1$, hence $A=\tfrac14$.

**Final Result**
$$
y(x)=c_1e^{-x}+c_2e^x+c_3xe^x+\tfrac14 x^2 e^x.
$$

---

### Exercise 7
$$
y''(x)-2y'(x)+y(x)=\sinh x.
$$

**Solution.** $P(\lambda)=\lambda^2-2\lambda+1=(\lambda-1)^2$,
$$
y_h=c_1e^x+c_2xe^x.
$$
Since $\sinh x=\tfrac12(e^x-e^{-x})$, split:

1) For $\tfrac12 e^x$ (resonance of multiplicity 2): try $y_{p1}=A x^2 e^x$ ⇒ $A=\tfrac14$.

2) For $-\tfrac12 e^{-x}$ (no resonance): try $y_{p2}=Be^{-x}$ ⇒ $B=-\tfrac18$.

**Final Result**
$$
y(x)=c_1e^x+c_2xe^x+\tfrac14 x^2 e^x-\tfrac18 e^{-x}.
$$

---

### Exercise 8
$$
y^{(4)}(x)-y^{(3)}(x)=\cos x+\sin(2x).
$$

**Solution.** Homogeneous: $P(\lambda)=\lambda^3(\lambda-1)$,
$$
y_h=c_1e^x+c_2+c_3x+c_4x^2.
$$
Split the forcing.

1) For $\cos x$: try $y_{p1}=A\cos x+B\sin x$. Substitution gives $A=B=\tfrac12$.

2) For $\sin2x$: try $y_{p2}=C\cos2x+D\sin2x$. Substitution gives $C=-\tfrac{1}{40}$, $D=\tfrac{1}{20}$.

**Final Result**
$$
y(x)=c_1e^x+c_2+c_3x+c_4x^2+\tfrac12(\sin x+\cos x)-\tfrac{1}{40}\cos2x+\tfrac{1}{20}\sin2x.
$$

---

### Exercise 9
$$
y^{(4)}(x)-2y^{(3)}(x)+y''(x)=x.
$$

**Solution.** $P(\lambda)=\lambda^2(\lambda-1)^2$,
$$
y_h=c_1+c_2x+c_3e^x+c_4x e^x.
$$
Forcing is polynomial and $P(0)=0$ with multiplicity 2 ⇒ try $y_p=x^2(Ax+B)$. Substitution gives $-12A+6Ax+2B=x$, hence $A=\tfrac16$, $B=1$.

**Final Result**
$$
y(x)=c_1+c_2x+c_3e^x+c_4x e^x+\tfrac16 x^3+x^2.
$$

---

### Exercise 10
$$
y''(x)+y(x)=\sec x=\frac{1}{\cos x}.
$$

**Solution.** Homogeneous: $y_h=c_1\cos x+c_2\sin x$.  
Variation of parameters with $y_1=\cos x$, $y_2=\sin x$ (Wronskian $W=1$) gives
$$
y_p=-y_1\!\int \frac{y_2\,g}{W}\,dx+y_2\!\int \frac{y_1\,g}{W}\,dx
=-\cos x\!\int \tan x\,dx+\sin x\!\int 1\,dx
$$
so
$$
y_p=\bigl(\log|\cos x|\bigr)\cos x + x\sin x,
$$
valid where $\cos x\neq 0$.

**Final Result**
$$
y(x)=c_1\cos x+c_2\sin x+\bigl(\log|\cos x|\bigr)\cos x+x\sin x,\qquad \cos x\neq 0.
$$

</div>

<div class="content-box">

## Related Pages in *Calculus I*

- [Complex Numbers](/university/math/calculus-1/complex-numbers/)  
- [Notable Limits](/university/math/calculus-1/notable-limits/)  
- [Limits with L’Hôpital’s Rule](/university/math/calculus-1/limits-hopital/)  
- [Limits with Taylor Expansion](/university/math/calculus-1/limits-taylor/)  
- [Sequences](/university/math/calculus-1/sequences/)  
- [Series](/university/math/calculus-1/series/)  
- [Continuity](/university/math/calculus-1/continuity/)  
- [Differentiability](/university/math/calculus-1/differentiability/)  
- [Integration by Parts](/university/math/calculus-1/integration-by-parts/)  
- [Integration by Substitution](/university/math/calculus-1/integration-by-substitution/)  
- [Cauchy Problems — ODEs](/university/math/calculus-1/odes-cauchy/)  

</div>
