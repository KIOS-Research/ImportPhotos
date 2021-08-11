<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="3.18.3-Zürich" maxScale="0" readOnly="0" labelsEnabled="0" minScale="100000000" simplifyLocal="1" hasScaleBasedVisibilityFlag="0" simplifyAlgorithm="0" simplifyDrawingHints="0" simplifyDrawingTol="1" simplifyMaxScale="1" styleCategories="AllStyleCategories">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
    <Private>0</Private>
  </flags>
  <temporal accumulate="0" startExpression="" fixedDuration="0" mode="0" enabled="0" durationField="" durationUnit="min" endField="Date" startField="Date" endExpression="">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <renderer-v2 enableorderby="0" type="RuleRenderer" symbollevels="0" forceraster="0">
    <rules key="{19ff78b9-5b95-47ce-a6f6-d7ed404baf2f}">
      <rule symbol="0" key="{3c96990c-e8c1-4804-a6f9-86c1d2622214}"/>
    </rules>
    <symbols>
      <symbol name="0" clip_to_extent="1" force_rhr="0" alpha="1" type="marker">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" value="" type="QString"/>
            <Option name="properties"/>
            <Option name="type" value="collection" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer class="SimpleMarker" enabled="1" pass="0" locked="0">
          <Option type="Map">
            <Option name="angle" value="0" type="QString"/>
            <Option name="color" value="97,97,97,255" type="QString"/>
            <Option name="horizontal_anchor_point" value="1" type="QString"/>
            <Option name="joinstyle" value="bevel" type="QString"/>
            <Option name="name" value="square" type="QString"/>
            <Option name="offset" value="0.00000000000000006,-10" type="QString"/>
            <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            <Option name="offset_unit" value="Pixel" type="QString"/>
            <Option name="outline_color" value="0,0,0,0" type="QString"/>
            <Option name="outline_style" value="solid" type="QString"/>
            <Option name="outline_width" value="0" type="QString"/>
            <Option name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            <Option name="outline_width_unit" value="Pixel" type="QString"/>
            <Option name="scale_method" value="diameter" type="QString"/>
            <Option name="size" value="5.4" type="QString"/>
            <Option name="size_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            <Option name="size_unit" value="Pixel" type="QString"/>
            <Option name="vertical_anchor_point" value="1" type="QString"/>
          </Option>
          <prop k="angle" v="0"/>
          <prop k="color" v="97,97,97,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="square"/>
          <prop k="offset" v="0.00000000000000006,-10"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="0,0,0,0"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="Pixel"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="5.4"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="Pixel"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option name="active" value="true" type="bool"/>
                  <Option name="expression" value="if(TO_REAL( &quot;Azimuth&quot; )=0,'',TO_REAL( &quot;Azimuth&quot; ))" type="QString"/>
                  <Option name="type" value="3" type="int"/>
                </Option>
                <Option name="size" type="Map">
                  <Option name="active" value="true" type="bool"/>
                  <Option name="expression" value="if( &quot;AZIMUTH&quot; !=0,5.4,0)" type="QString"/>
                  <Option name="type" value="3" type="int"/>
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="SimpleMarker" enabled="1" pass="0" locked="0">
          <Option type="Map">
            <Option name="angle" value="0" type="QString"/>
            <Option name="color" value="255,255,255,255" type="QString"/>
            <Option name="horizontal_anchor_point" value="1" type="QString"/>
            <Option name="joinstyle" value="bevel" type="QString"/>
            <Option name="name" value="square" type="QString"/>
            <Option name="offset" value="0,0" type="QString"/>
            <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            <Option name="offset_unit" value="Pixel" type="QString"/>
            <Option name="outline_color" value="97,97,97,255" type="QString"/>
            <Option name="outline_style" value="solid" type="QString"/>
            <Option name="outline_width" value="0" type="QString"/>
            <Option name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            <Option name="outline_width_unit" value="Pixel" type="QString"/>
            <Option name="scale_method" value="diameter" type="QString"/>
            <Option name="size" value="14" type="QString"/>
            <Option name="size_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            <Option name="size_unit" value="Pixel" type="QString"/>
            <Option name="vertical_anchor_point" value="1" type="QString"/>
          </Option>
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="square"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="97,97,97,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="Pixel"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="14"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="Pixel"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option name="active" value="false" type="bool"/>
                  <Option name="expression" value="if(TO_REAL( &quot;Azimuth&quot; )=0,'',TO_REAL( &quot;Azimuth&quot; ))" type="QString"/>
                  <Option name="type" value="3" type="int"/>
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="SimpleMarker" enabled="1" pass="0" locked="0">
          <Option type="Map">
            <Option name="angle" value="0" type="QString"/>
            <Option name="color" value="97,97,97,255" type="QString"/>
            <Option name="horizontal_anchor_point" value="1" type="QString"/>
            <Option name="joinstyle" value="bevel" type="QString"/>
            <Option name="name" value="triangle" type="QString"/>
            <Option name="offset" value="-2,1" type="QString"/>
            <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            <Option name="offset_unit" value="Pixel" type="QString"/>
            <Option name="outline_color" value="0,0,0,0" type="QString"/>
            <Option name="outline_style" value="solid" type="QString"/>
            <Option name="outline_width" value="0" type="QString"/>
            <Option name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            <Option name="outline_width_unit" value="Pixel" type="QString"/>
            <Option name="scale_method" value="diameter" type="QString"/>
            <Option name="size" value="5" type="QString"/>
            <Option name="size_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            <Option name="size_unit" value="Pixel" type="QString"/>
            <Option name="vertical_anchor_point" value="1" type="QString"/>
          </Option>
          <prop k="angle" v="0"/>
          <prop k="color" v="97,97,97,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="triangle"/>
          <prop k="offset" v="-2,1"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="0,0,0,0"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="Pixel"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="5"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="Pixel"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option name="active" value="false" type="bool"/>
                  <Option name="expression" value="if(TO_REAL( &quot;Azimuth&quot; )=0,'',TO_REAL( &quot;Azimuth&quot; ))" type="QString"/>
                  <Option name="type" value="3" type="int"/>
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="SimpleMarker" enabled="1" pass="0" locked="0">
          <Option type="Map">
            <Option name="angle" value="0" type="QString"/>
            <Option name="color" value="97,97,97,255" type="QString"/>
            <Option name="horizontal_anchor_point" value="1" type="QString"/>
            <Option name="joinstyle" value="bevel" type="QString"/>
            <Option name="name" value="triangle" type="QString"/>
            <Option name="offset" value="2,0" type="QString"/>
            <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            <Option name="offset_unit" value="Pixel" type="QString"/>
            <Option name="outline_color" value="0,0,0,0" type="QString"/>
            <Option name="outline_style" value="solid" type="QString"/>
            <Option name="outline_width" value="0" type="QString"/>
            <Option name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            <Option name="outline_width_unit" value="Pixel" type="QString"/>
            <Option name="scale_method" value="diameter" type="QString"/>
            <Option name="size" value="7" type="QString"/>
            <Option name="size_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            <Option name="size_unit" value="Pixel" type="QString"/>
            <Option name="vertical_anchor_point" value="1" type="QString"/>
          </Option>
          <prop k="angle" v="0"/>
          <prop k="color" v="97,97,97,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="triangle"/>
          <prop k="offset" v="2,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="0,0,0,0"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="Pixel"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="7"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="Pixel"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option name="active" value="false" type="bool"/>
                  <Option name="expression" value="if(TO_REAL( &quot;Azimuth&quot; )=0,'',TO_REAL( &quot;Azimuth&quot; ))" type="QString"/>
                  <Option name="type" value="3" type="int"/>
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="SimpleMarker" enabled="1" pass="0" locked="0">
          <Option type="Map">
            <Option name="angle" value="0" type="QString"/>
            <Option name="color" value="97,97,97,255" type="QString"/>
            <Option name="horizontal_anchor_point" value="1" type="QString"/>
            <Option name="joinstyle" value="bevel" type="QString"/>
            <Option name="name" value="square" type="QString"/>
            <Option name="offset" value="-1,-3" type="QString"/>
            <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            <Option name="offset_unit" value="Pixel" type="QString"/>
            <Option name="outline_color" value="0,0,0,0" type="QString"/>
            <Option name="outline_style" value="solid" type="QString"/>
            <Option name="outline_width" value="0" type="QString"/>
            <Option name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            <Option name="outline_width_unit" value="Pixel" type="QString"/>
            <Option name="scale_method" value="diameter" type="QString"/>
            <Option name="size" value="2" type="QString"/>
            <Option name="size_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            <Option name="size_unit" value="Pixel" type="QString"/>
            <Option name="vertical_anchor_point" value="1" type="QString"/>
          </Option>
          <prop k="angle" v="0"/>
          <prop k="color" v="97,97,97,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="square"/>
          <prop k="offset" v="-1,-3"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="0,0,0,0"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="Pixel"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="Pixel"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option name="active" value="false" type="bool"/>
                  <Option name="expression" value="if(TO_REAL( &quot;Azimuth&quot; )=0,'',TO_REAL( &quot;Azimuth&quot; ))" type="QString"/>
                  <Option name="type" value="3" type="int"/>
                </Option>
                <Option name="size" type="Map">
                  <Option name="active" value="false" type="bool"/>
                  <Option name="expression" value="if( &quot;AZIMUTH&quot; !=0,2,0)" type="QString"/>
                  <Option name="type" value="3" type="int"/>
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <customproperties>
    <property value="ID" key="dualview/previewExpressions"/>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory sizeScale="3x:0,0,0,0,0,0" lineSizeScale="3x:0,0,0,0,0,0" width="15" backgroundColor="#ffffff" penAlpha="255" penColor="#000000" opacity="1" lineSizeType="MM" minScaleDenominator="0" backgroundAlpha="255" spacingUnitScale="3x:0,0,0,0,0,0" direction="1" enabled="0" labelPlacementMethod="XHeight" barWidth="5" rotationOffset="270" maxScaleDenominator="1e+08" height="15" diagramOrientation="Up" sizeType="MM" scaleDependency="Area" penWidth="0" spacingUnit="MM" showAxis="0" spacing="0" minimumSize="0" scaleBasedVisibility="0">
      <fontProperties description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" style=""/>
      <attribute color="#000000" field="" label=""/>
      <axisSymbol>
        <symbol name="" clip_to_extent="1" force_rhr="0" alpha="1" type="line">
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <layer class="SimpleLine" enabled="1" pass="0" locked="0">
            <Option type="Map">
              <Option name="align_dash_pattern" value="0" type="QString"/>
              <Option name="capstyle" value="square" type="QString"/>
              <Option name="customdash" value="5;2" type="QString"/>
              <Option name="customdash_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
              <Option name="customdash_unit" value="MM" type="QString"/>
              <Option name="dash_pattern_offset" value="0" type="QString"/>
              <Option name="dash_pattern_offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
              <Option name="dash_pattern_offset_unit" value="MM" type="QString"/>
              <Option name="draw_inside_polygon" value="0" type="QString"/>
              <Option name="joinstyle" value="bevel" type="QString"/>
              <Option name="line_color" value="35,35,35,255" type="QString"/>
              <Option name="line_style" value="solid" type="QString"/>
              <Option name="line_width" value="0.26" type="QString"/>
              <Option name="line_width_unit" value="MM" type="QString"/>
              <Option name="offset" value="0" type="QString"/>
              <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
              <Option name="offset_unit" value="MM" type="QString"/>
              <Option name="ring_filter" value="0" type="QString"/>
              <Option name="tweak_dash_pattern_on_corners" value="0" type="QString"/>
              <Option name="use_custom_dash" value="0" type="QString"/>
              <Option name="width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            </Option>
            <prop k="align_dash_pattern" v="0"/>
            <prop k="capstyle" v="square"/>
            <prop k="customdash" v="5;2"/>
            <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
            <prop k="customdash_unit" v="MM"/>
            <prop k="dash_pattern_offset" v="0"/>
            <prop k="dash_pattern_offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
            <prop k="dash_pattern_offset_unit" v="MM"/>
            <prop k="draw_inside_polygon" v="0"/>
            <prop k="joinstyle" v="bevel"/>
            <prop k="line_color" v="35,35,35,255"/>
            <prop k="line_style" v="solid"/>
            <prop k="line_width" v="0.26"/>
            <prop k="line_width_unit" v="MM"/>
            <prop k="offset" v="0"/>
            <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
            <prop k="offset_unit" v="MM"/>
            <prop k="ring_filter" v="0"/>
            <prop k="tweak_dash_pattern_on_corners" v="0"/>
            <prop k="use_custom_dash" v="0"/>
            <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
            <data_defined_properties>
              <Option type="Map">
                <Option name="name" value="" type="QString"/>
                <Option name="properties"/>
                <Option name="type" value="collection" type="QString"/>
              </Option>
            </data_defined_properties>
          </layer>
        </symbol>
      </axisSymbol>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings showAll="1" priority="0" zIndex="0" linePlacementFlags="18" obstacle="0" dist="0" placement="0">
    <properties>
      <Option type="Map">
        <Option name="name" value="" type="QString"/>
        <Option name="properties"/>
        <Option name="type" value="collection" type="QString"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <legend type="default-vector"/>
  <referencedLayers/>
  <fieldConfiguration>
    <field name="ID" configurationFlags="None">
      <editWidget type="Hidden">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Name" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Date" configurationFlags="None">
      <editWidget type="DateTime">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Time" configurationFlags="None">
      <editWidget type="DateTime">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Lon" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Lat" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Altitude" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="North" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Azimuth" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Camera Mak" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Camera Mod" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Title" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Comment" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Path" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="RelPath" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Timestamp" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Images" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias name="" field="ID" index="0"/>
    <alias name="" field="Name" index="1"/>
    <alias name="" field="Date" index="2"/>
    <alias name="" field="Time" index="3"/>
    <alias name="" field="Lon" index="4"/>
    <alias name="" field="Lat" index="5"/>
    <alias name="" field="Altitude" index="6"/>
    <alias name="" field="North" index="7"/>
    <alias name="" field="Azimuth" index="8"/>
    <alias name="" field="Camera Mak" index="9"/>
    <alias name="" field="Camera Mod" index="10"/>
    <alias name="" field="Title" index="11"/>
    <alias name="" field="Comment" index="12"/>
    <alias name="" field="Path" index="13"/>
    <alias name="" field="RelPath" index="14"/>
    <alias name="" field="Timestamp" index="15"/>
    <alias name="" field="Images" index="16"/>
  </aliases>
  <defaults>
    <default expression="" field="ID" applyOnUpdate="0"/>
    <default expression="" field="Name" applyOnUpdate="0"/>
    <default expression="" field="Date" applyOnUpdate="0"/>
    <default expression="" field="Time" applyOnUpdate="0"/>
    <default expression="" field="Lon" applyOnUpdate="0"/>
    <default expression="" field="Lat" applyOnUpdate="0"/>
    <default expression="" field="Altitude" applyOnUpdate="0"/>
    <default expression="" field="North" applyOnUpdate="0"/>
    <default expression="" field="Azimuth" applyOnUpdate="0"/>
    <default expression="" field="Camera Mak" applyOnUpdate="0"/>
    <default expression="" field="Camera Mod" applyOnUpdate="0"/>
    <default expression="" field="Title" applyOnUpdate="0"/>
    <default expression="" field="Comment" applyOnUpdate="0"/>
    <default expression="" field="Path" applyOnUpdate="0"/>
    <default expression="" field="RelPath" applyOnUpdate="0"/>
    <default expression="" field="Timestamp" applyOnUpdate="0"/>
    <default expression="" field="Images" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint constraints="0" notnull_strength="0" field="ID" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="Name" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="Date" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="Time" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="Lon" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="Lat" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="Altitude" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="North" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="Azimuth" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="Camera Mak" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="Camera Mod" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="Title" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="Comment" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="Path" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="RelPath" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="Timestamp" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="Images" unique_strength="0" exp_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="ID" exp="" desc=""/>
    <constraint field="Name" exp="" desc=""/>
    <constraint field="Date" exp="" desc=""/>
    <constraint field="Time" exp="" desc=""/>
    <constraint field="Lon" exp="" desc=""/>
    <constraint field="Lat" exp="" desc=""/>
    <constraint field="Altitude" exp="" desc=""/>
    <constraint field="North" exp="" desc=""/>
    <constraint field="Azimuth" exp="" desc=""/>
    <constraint field="Camera Mak" exp="" desc=""/>
    <constraint field="Camera Mod" exp="" desc=""/>
    <constraint field="Title" exp="" desc=""/>
    <constraint field="Comment" exp="" desc=""/>
    <constraint field="Path" exp="" desc=""/>
    <constraint field="RelPath" exp="" desc=""/>
    <constraint field="Timestamp" exp="" desc=""/>
    <constraint field="Images" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortOrder="1" sortExpression="&quot;Camera Model&quot;">
    <columns>
      <column name="ID" width="-1" hidden="0" type="field"/>
      <column width="-1" hidden="1" type="actions"/>
      <column name="Name" width="-1" hidden="0" type="field"/>
      <column name="Date" width="-1" hidden="0" type="field"/>
      <column name="Time" width="-1" hidden="0" type="field"/>
      <column name="Lon" width="-1" hidden="0" type="field"/>
      <column name="Lat" width="-1" hidden="0" type="field"/>
      <column name="Altitude" width="-1" hidden="0" type="field"/>
      <column name="North" width="-1" hidden="0" type="field"/>
      <column name="Azimuth" width="-1" hidden="0" type="field"/>
      <column name="Path" width="-1" hidden="0" type="field"/>
      <column name="Camera Mak" width="-1" hidden="0" type="field"/>
      <column name="Camera Mod" width="-1" hidden="0" type="field"/>
      <column name="Title" width="-1" hidden="0" type="field"/>
      <column name="Comment" width="-1" hidden="0" type="field"/>
      <column name="RelPath" width="-1" hidden="0" type="field"/>
      <column name="Timestamp" width="-1" hidden="0" type="field"/>
      <column name="Images" width="-1" hidden="0" type="field"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.

Use this function to add extra logic to your forms.

Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field name="ALTITUDE" editable="1"/>
    <field name="AZIMUTH" editable="1"/>
    <field name="Altitude" editable="1"/>
    <field name="Azimuth" editable="1"/>
    <field name="CAMERA MAK" editable="1"/>
    <field name="CAMERA MOD" editable="1"/>
    <field name="Camera Mak" editable="1"/>
    <field name="Camera Maker" editable="1"/>
    <field name="Camera Mod" editable="1"/>
    <field name="Camera Model" editable="1"/>
    <field name="Comment" editable="1"/>
    <field name="DATE" editable="1"/>
    <field name="Date" editable="1"/>
    <field name="ID" editable="1"/>
    <field name="Images" editable="1"/>
    <field name="LAT" editable="1"/>
    <field name="LON" editable="1"/>
    <field name="Lat" editable="1"/>
    <field name="Lon" editable="1"/>
    <field name="NAME" editable="1"/>
    <field name="NORTH" editable="1"/>
    <field name="Name" editable="1"/>
    <field name="North" editable="1"/>
    <field name="PATH" editable="1"/>
    <field name="Path" editable="1"/>
    <field name="RelPath" editable="1"/>
    <field name="TIME" editable="1"/>
    <field name="Time" editable="1"/>
    <field name="Timestamp" editable="1"/>
    <field name="Title" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="ALTITUDE" labelOnTop="0"/>
    <field name="AZIMUTH" labelOnTop="0"/>
    <field name="Altitude" labelOnTop="0"/>
    <field name="Azimuth" labelOnTop="0"/>
    <field name="CAMERA MAK" labelOnTop="0"/>
    <field name="CAMERA MOD" labelOnTop="0"/>
    <field name="Camera Mak" labelOnTop="0"/>
    <field name="Camera Maker" labelOnTop="0"/>
    <field name="Camera Mod" labelOnTop="0"/>
    <field name="Camera Model" labelOnTop="0"/>
    <field name="Comment" labelOnTop="0"/>
    <field name="DATE" labelOnTop="0"/>
    <field name="Date" labelOnTop="0"/>
    <field name="ID" labelOnTop="0"/>
    <field name="Images" labelOnTop="0"/>
    <field name="LAT" labelOnTop="0"/>
    <field name="LON" labelOnTop="0"/>
    <field name="Lat" labelOnTop="0"/>
    <field name="Lon" labelOnTop="0"/>
    <field name="NAME" labelOnTop="0"/>
    <field name="NORTH" labelOnTop="0"/>
    <field name="Name" labelOnTop="0"/>
    <field name="North" labelOnTop="0"/>
    <field name="PATH" labelOnTop="0"/>
    <field name="Path" labelOnTop="0"/>
    <field name="RelPath" labelOnTop="0"/>
    <field name="TIME" labelOnTop="0"/>
    <field name="Time" labelOnTop="0"/>
    <field name="Timestamp" labelOnTop="0"/>
    <field name="Title" labelOnTop="0"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>"Name"</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>
