using Convex
T = 1000

function optimizer(z, lambda)

    w = Variable(1) # Variable who storage the wt
    problem = minimize(sum((z*w)+((lambda/2)*square(w))), [w >= -1.00, w <= 1.00])
    solve!(problem)
    return   w.value
end

function adversary(adversary, w)
    #First adversary
    if adversary == 1
        if w < 0
            return -1.0
        else
            return 1.0
        end
    #Second adversary
    else
        zt = [-1.0, 1.0]
        sort = rand(1:2,1)
        return zt[sort]
    end

end

function FTL(adv_)
    z = Array{Float64,1}()
    w = Array{Float64,1}()
    # In the first make decision
    append!(w, 0.0)
    print(w[1])
    adv = adversary(adv_, w[1])
    append!(z,adv)

    for t in range(2,T-1)
        append!(w, optimizer(z[1:(t-1)], 0.0))
        append!(z, adversary(adv_, w[t]))
    end
    return w, z
end

function FTRL(adv_)
    z = Array{Float64,1}()
    w = Array{Float64,1}()
    n = 0.3 # taxa de aprendizagem
    append!(w, optimizer(0.0,(1/n) ))
    append!(z, adversary(adv_, w[1]))


    for t in range(2,T-1)
        println(t)
        append!(w, optimizer(z[1:(t-1)], (1/n)))
        append!(z, adversary(adv_, w[t]))

    end
    return w, z
end

function total_lost(z, w)

    total_lost =0

    for t in range(1,T)
        total_lost+= (z[t]*w[t])
    end
    return total_lost
end

function main()

    w1, z1 = FTL(2)
    w2, z2 = FTRL(2)
    #w = optimizer([1.0, -1.0], 0.0)
    println("Follow the Leader")
    println("W = ", w1)
    println("Z = ", z1)
    println("Follow the Regularized Leader")
    println("W = ", w2)
    println("Z = ", z2)
    lost1 = total_lost(w1, z1)
    println("Total Lost - Follow the Leader: ", lost1)
    lost2 = total_lost(w2, z2)
    println("Total Lost - Follow the Regularized Leader: ", lost2)

end

main()
