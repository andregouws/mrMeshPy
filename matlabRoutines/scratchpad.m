% a scratchpad of test commands used during mrMeshPy development

 Callback: MSH = viewGet(VOLUME{1}, 'Mesh');
 vertexGrayMap = mrmMapVerticesToGray( meshGet(MSH, 'vertices'), viewGet(VOLUME{1}, 'nodes'), viewGet(VOLUME{1}, 'mmPerVox'), viewGet(VOLUME{1}, 'edges') ); 
 MSH = meshSet(MSH, 'vertexgraymap', vertexGrayMap); 
 VOLUME{1} = viewSet(VOLUME{1}, 'Mesh', MSH); 
 clear MSH vertexGrayMap



msh = mrmBuildMeshMatlab(cFile,1.0);
msh.colors(4,:) = 255;
msh.vertexGrayMap = mrmMapVerticesToGray( meshGet(msh, 'vertices'), viewGet(VOLUME{1}, 'nodes'), viewGet(VOLUME{1}, 'mmPerVox'), viewGet(VOLUME{1}, 'edges') )
VOLUME{1} = rmfield(VOLUME{1},'mesh')
