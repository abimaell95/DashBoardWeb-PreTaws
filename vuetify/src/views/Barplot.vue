<script>

import { Line } from 'vue-chartjs'

export default {
  extends: Line,
  props: {
    chartdata: {
      type: Object,
      default: null
    },
    options: {
      type: Object,
      default: null
    }
  },
  mounted () {
    this.renderChart(this.chartdata, this.options)
  }
}
import Chart from '@/components/Chart'

export default {
  name: 'VueChartJS',
  components: {
    Chart
  }, data: () => ({
    items: ['Ecuador', 'Mexico', 'Venezuela'],select
  }),
}
</script>

