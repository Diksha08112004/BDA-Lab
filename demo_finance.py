import finance as fin

def main():
    # Test simple interest
    principal = 10000
    rate = 5  # 5%
    time = 3   # 3 years
    
    si = fin.simple_interest(principal, rate, time)
    print(f"=== Simple Interest ===")
    print(f"Principal: ₹{principal:,}")
    print(f"Rate: {rate}%")
    print(f"Time: {time} years")
    print(f"Simple Interest: ₹{si:,.2f}")
    print(f"Total Amount: ₹{principal + si:,.2f}")
    
    # Test compound interest (compounded annually)
    print("\n=== Compound Interest (Annually) ===")
    ci_annual = fin.compound_interest(principal, rate, time)
    print(f"Principal: ₹{principal:,}")
    print(f"Rate: {rate}% (compounded annually)")
    print(f"Time: {time} years")
    print(f"Compound Interest: ₹{ci_annual:,.2f}")
    print(f"Total Amount: ₹{principal + ci_annual:,.2f}")
    
    # Test compound interest (compounded quarterly)
    print("\n=== Compound Interest (Quarterly) ===")
    n = 4  # quarterly compounding
    ci_quarterly = fin.compound_interest(principal, rate, time, n)
    print(f"Principal: ₹{principal:,}")
    print(f"Rate: {rate}% (compounded quarterly)")
    print(f"Time: {time} years")
    print(f"Compound Interest: ₹{ci_quarterly:,.2f}")
    print(f"Total Amount: ₹{principal + ci_quarterly:,.2f}")
    
    # Compare simple vs compound interest
    print("\n=== Comparison ===")
    print(f"Difference between Compound and Simple Interest:")
    print(f"- Annually: ₹{ci_annual - si:,.2f} more")
    print(f"- Quarterly: ₹{ci_quarterly - si:,.2f} more")

if __name__ == "__main__":
    main()
