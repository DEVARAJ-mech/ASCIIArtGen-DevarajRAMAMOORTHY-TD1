const plotData = [{
    z: zData,
    x: xData,
    y: yData,
    type: 'surface',
    colorscale: 'Cividis', // Change to a visually appealing scale
}];

const layout = {
    title: '3D ASCII Art Visualization',
    scene: {
        xaxis: { title: 'Width' },
        yaxis: { title: 'Height' },
        zaxis: { title: 'Character Intensity' },
    }
};

Plotly.newPlot(plotContainer, plotData, layout);