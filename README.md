# Fuzzy
## Only for fuzzy related problem 
### Fuzzy Set and Logic:
---------------------------
Fuzzy Set and Logic.

 1.⁠ ⁠WAP to compute Support (crisp) of a Fuzzy Set.
 
 2.⁠ ⁠WAP to compute alpha-level set of a Fuzzy Set (alpha is input).
 
 3.⁠ ⁠WAP to calculate scalar and relative cardinality
 
 4.⁠ ⁠WAP to compute Union of two given Fuzzy sets
 
 5.⁠ ⁠WAP to compute Intersection of two given Fuzzy sets
 
 6.⁠ ⁠WAP to compute complement of a fuzzy set
 
 7.⁠ ⁠WAP to check whether a Fuzzy set is included in the other (subset)
 
 8.⁠ ⁠WAP to compute Cartesian product of two Fuzzy sets
 
 9.⁠ ⁠WAP to compute mᵗʰ power of a Fuzzy set
 
10.⁠ ⁠WAP to compute algebraic / probabilistic sum of two fuzzy sets

11.⁠ ⁠WAP to compute bounded sum of two fuzzy sets

12.⁠ ⁠WAP to compute bounded difference of two fuzzy sets

13.⁠ ⁠WAP to compute algebraic product of two fuzzy sets

---------------------------
## Mathematical repersentations
### Support (crisp) of a Fuzzy Set:


---

## 📌 Support (Crisp) of a Fuzzy Set

In fuzzy set theory, the **support** of a fuzzy set refers to all elements in the universe whose membership values are greater than zero. Although a fuzzy set allows elements to have degrees of membership between 0 and 1, the support extracts only those elements that actually belong to the set in some degree (i.e., with non-zero membership). The result is a **crisp set**, meaning it contains only elements without any membership values.

### 🧮 Mathematical Representation

Let a fuzzy set ( A ) be defined on a universe ( X ) with a membership function:

```
μA(x) : X → [0,1]
```

Then, the support of the fuzzy set ( A ) is given by:

```
Supp(A) = { x ∈ X | μA(x) > 0 }
```

### 📊 Example

```
A = { (a, 0.2), (b, 0), (c, 0.7), (d, 0) }
```

Then:

```
Supp(A) = { a, c }
```

✔ Only elements with membership values greater than zero are included.

---



