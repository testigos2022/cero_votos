
module CeroVotos
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1"

include("jl/cerovotos.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "cero_votos",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "async-CeroVotos.js",
    external_url = "https://unpkg.com/cero_votos@0.0.1/cero_votos/async-CeroVotos.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-CeroVotos.js.map",
    external_url = "https://unpkg.com/cero_votos@0.0.1/cero_votos/async-CeroVotos.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "cero_votos.min.js",
    external_url = "https://unpkg.com/cero_votos@0.0.1/cero_votos/cero_votos.min.js",
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "cero_votos.min.js.map",
    external_url = "https://unpkg.com/cero_votos@0.0.1/cero_votos/cero_votos.min.js.map",
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
