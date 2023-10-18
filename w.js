function employee(name,phno,bsal)
{
    this.name=name
    this.phno=phno
    this.basal=bsal
    let bonus=501
    this.bal=function()
             {
                console.log("name is "+this.name+"phno is "+this.phno)
                actual()
             }
        let actual=function()
            {
                var final=bsal+bonus
                console.log("your sal is"+final)
            }
        
}
let b=new employee("bhabani",811431,5000)
b.bal()
b.phno
b.bonus