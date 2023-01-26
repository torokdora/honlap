function lnko (a, b) {
if (a > b) return lnko (a - b, b)
if (b > a) return (a, b-a)
return a
}

function f() {
    k = lnko (b, d)
    csz = b/k
    asz = d/k
    sz = a*asz + c*csz
    n = asz*csz*k
    e = lnko (sz, n)
    console.log(sz, n, e)
    document.getElementById("sz").innerHTML = sz / e
    document.getElementById("n").innerHTML = n/ e
}