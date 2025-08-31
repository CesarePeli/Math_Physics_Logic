---
layout: default
date: 2025-08-30
title: "Solved Exercises — Limits with L’Hôpital’s Rule"
meta-description: "Ten fully worked examples solved strictly with L’Hôpital’s rule: 0/0 and ∞/∞ forms, repeated applications, and algebraic rewrites to quotients."
permalink: "/university/math/calculus-1/limits-hopital/"
background_image: "/images/limiti.png"
---

<div class="content-box">

## Hôpital's Theorem

Let f, g be two functions defined in a neighborhood of c, except possibly at c, such that  

$$
\lim_{x \to c} f(x) = \lim_{x \to c} g(x) = L,
$$  

with L = 0 or L = +∞ or L = −∞.  
If f and g are differentiable in a neighborhood of c, except possibly at c, with g′ ≠ 0, and if the following limit exists (finite or infinite):  

$$
\lim_{x \to c} \frac{f'(x)}{g'(x)},
$$  

then also  

$$
\lim_{x \to c} \frac{f(x)}{g(x)}
$$  

exists and equals the previous one.

</div>

---

<div class="content-box">

## Exercises

**Ex 1.**  

$$
\lim_{x \to 0}\frac{e^{x^{x}}-e}{x}.
$$  

**Solution**  
Indeterminate form 0/0. Apply Hôpital:  

$$(x^{x})' = (e^{x \log x})' = (\log x +1)x^{x}.$$  

So  

$$
\lim_{x \to 0}\frac{e^{x^{x}}-e}{x} \overset{H}{=}
\lim_{x \to 0} (\log x+1)x^{x} e^{x^x} = -\infty .
$$  

Indeed,  

$$
\lim_{x \to 0} x^x = e^0 = 1.
$$  

---

**Ex 2.**  

$$
\lim_{x \to 0}\Bigl(\frac{\sin x}{x}\Bigr)^{1/x^{2}}.
$$  

**Solution**  

$$
\lim_{x \to 0}\Bigl(\frac{\sin x}{x}\Bigr)^{1/x^{2}}
= \lim_{x \to 0} e^{\frac{\log(\sin x/x)}{x^2}}
= e^{-1/6}.
$$  

---

**Ex 3.**  

$$
\lim_{x \to 0}\frac{e^{\sin x}-\cos x}{e^{\cos x}-e\log(x+e)} .
$$  

**Solution**  
Indeterminate form 0/0:  

$$
\lim_{x \to 0}\frac{e^{\sin x}-\cos x}{e^{\cos x}-e\log(x+e)}
\overset{H}{=}
\lim_{x \to 0} \frac{\cos x \, e^{\sin x} + \sin x}{-\sin x \, e^{\cos x} - \tfrac{e}{x+e}} = -1 .
$$  

---

**Ex 4.**  

$$
\lim_{x \to -1}\frac{e^{\sqrt{1-3x}}-e^{\sqrt{3-x}}}{e^{x}-e^{2x+1}} .
$$  

**Solution**  

$$
\lim_{x \to -1}\frac{e^{\sqrt{1-3x}}-e^{\sqrt{3-x}}}{e^{x}-e^{2x+1}}
\overset{H}{=}
\frac{-\tfrac{3}{4}e^{2}+\tfrac{e^{2}}{4}}{\tfrac{1}{e}-\tfrac{2}{e}}
= \frac{e^3}{2}.
$$  

---

**Ex 5.**  

$$
\lim_{x \to 1^{-}} \log(x)\log(1-x).
$$  

**Solution**  

$$
\lim_{x \to 1^{-}} \log(x)\log(1-x) 
= \lim_{x \to 1^{-}} \frac{\log(1-x)}{1/\log x}
\overset{H}{=}
\lim_{x \to 1^{-}} \frac{-\tfrac{1}{1-x}}{-1/(x \log^2 x)} = 0.
$$  

---

**Ex 6.**  

$$
\lim_{x \to 3^{+}}\frac{\sqrt{x}-\sqrt{3}+\sqrt{x-3}}{\sqrt{x^{2}-9}} .
$$  

**Solution**  

$$
\lim_{x \to 3^{+}}\frac{\sqrt{x}-\sqrt{3}+\sqrt{x-3}}{\sqrt{x^{2}-9}}
= \frac{1}{\sqrt{6}} .
$$  

Indeed,  

$$
\lim_{x \to 3^+} \frac{\sqrt{x}-\sqrt{3}}{\sqrt{x-3}}
\overset{H}{=}
\lim_{x \to 3^+} \frac{1/(2\sqrt{x})}{1/(2\sqrt{x-3})} = 0.
$$  

---

**Ex 7.**  

$$
\lim_{x \to 0^{+}}\frac{x^{2}-\arctan(x^{2})}{x(1-\cos x)^{3}} .
$$  

**Solution**  

$$
\lim_{x \to 0^{+}}\frac{x^{2}-\arctan(x^{2})}{x(1-\cos x)^{3}}
\overset{H}{=}
\lim_{x \to 0^+} \frac{2x - \tfrac{2x}{1+x^4}}{(1-\cos x)^3+3x(1-\cos x)^2\sin x}
= +\infty .
$$  

---

**Ex 8.**  

$$
\lim_{x \to 0}\frac{e^{x}-\cos x-\sin x}{e^{x^{2}}-e^{x^{3}}} .
$$  

**Solution**  
Taylor near 0:  

$$
e^x = 1+x+\tfrac{x^2}{2}+\tfrac{x^3}{6}+o(x^3), \quad 
\cos x = 1-\tfrac{x^2}{2}+o(x^2), \quad
\sin x = x-\tfrac{x^3}{6}+o(x^3).
$$  

So numerator ∼ x² + x³/6, denominator ∼ x² − x³.  
Hence limit = 1.  

---

**Ex 9.**  

$$
\lim_{x \to 0}\frac{1-\cos x+\log(\cos x)}{x^{4}} .
$$  

**Solution**  
Expansions:  

$$
\cos x = 1-\tfrac{x^2}{2}+\tfrac{x^4}{24}+o(x^4),
$$  

$$
\log(\cos x) = -\tfrac{x^2}{2} - \tfrac{x^4}{12}+o(x^4).
$$  

So numerator ∼ −⅛x⁴.  

$$
\lim_{x \to 0}\frac{1-\cos x+\log(\cos x)}{x^4} = -\tfrac{1}{8}.
$$  

---

**Ex 10.**  

$$
\lim_{x \to 0}\frac{e^{x^{2}}-\cos^{2}x}{\sin^{2}x}.
$$  

**Solution (two methods)**  

**By Hôpital:**  

$$
\lim_{x \to 0}\frac{e^{x^{2}}-\cos^{2}x}{\sin^{2}x}
\overset{H}{=}
\lim_{x \to 0}\frac{2xe^{x^2}+2\cos x \sin x}{2\cos x \sin x} 
= \lim_{x \to 0} \frac{x}{\sin x}\cdot\frac{e^{x^2}}{\cos x} +1 = 2.
$$  

**By Taylor:**  

$$
e^{x^2}=1+x^2+o(x^2), \quad \cos^2 x = 1-x^2+o(x^2).
$$  

So numerator ∼ 2x², denominator ∼ x², ratio = 2.  

</div>

---

<div class="content-box">

## Explore more topics in Calculus 1

- [Complex Numbers]({{ "/university/math/calculus-1/complex-numbers/" | relative_url }})  
- [Notable Limits](/university/math/calculus-1/notable-limits/)  
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
