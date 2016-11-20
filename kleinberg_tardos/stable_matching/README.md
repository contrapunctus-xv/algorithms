Stable Matching Algorithm on finding a stable match between two genders.
The desired situation is that for M men and W women to be matched to each other
such that m would not leave w' for w' and w would not leave m for w'. 

This is will be explored in two implementions: one with just linked lists 
and arrays and the other with priority queues.

Paraphrahsed pseudo Code from Kleinberg and Tardos

```
Initially all men and women are free to engage

while there are unengaged men
    choose such a man m
    get a w that is listed the highest on m's list
    if w is free then
        m and w are engaged
    else
        if w prefers m' to m then 
            m remains free
        else
            m and w are engaged
            and m' is free     
return the set of engaged pairs
```