WITH final AS (
  SELECT * FROM {{ ref('dim_movies_with_tags') }}
)

SELECT
  * from final