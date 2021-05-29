def mrp(buyingprice , sellingprice , **tax):
    print("Buying price is : ",buyingprice);
    print("Selling price is : ",sellingprice);
    for key , value in tax.items():
        print("Key is ",key , type(key));
        print("Value is ",value , type(value));

mrp(100 , 250);
mrp(100 , 250 , sgst=5 , cgst = 7);
