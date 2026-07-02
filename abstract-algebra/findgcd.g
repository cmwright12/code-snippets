FindGcd:=function()
    local a,b;
    a:=Random([21..200]);
    b:=Random([11..20]);

    while a mod b = 0 do
        a:=Random([21..200]);
        b:=Random([11..20]);
    od;
    Print("a=",a,", b=",b,"\n");
    ShowGcd(a,b);
    end;

for i in [1..5] do
    FindGcd();
od;
