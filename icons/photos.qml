<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis styleCategories="AllStyleCategories" simplifyMaxScale="1" simplifyLocal="1" maxScale="0" readOnly="0" version="3.18.2-Zürich" simplifyAlgorithm="0" labelsEnabled="0" minScale="100000000" simplifyDrawingHints="0" simplifyDrawingTol="1" hasScaleBasedVisibilityFlag="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
    <Private>0</Private>
  </flags>
  <temporal durationUnit="min" mode="0" accumulate="0" startExpression="" fixedDuration="0" endField="" enabled="0" durationField="" startField="" endExpression="">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <renderer-v2 symbollevels="0" enableorderby="0" type="singleSymbol" forceraster="0">
    <symbols>
      <symbol alpha="1" force_rhr="0" name="0" clip_to_extent="1" type="marker">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer locked="0" pass="0" class="SimpleMarker" enabled="1">
          <Option type="Map">
            <Option value="0" name="angle" type="QString"/>
            <Option value="97,97,97,255" name="color" type="QString"/>
            <Option value="1" name="horizontal_anchor_point" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="square" name="name" type="QString"/>
            <Option value="0.00000000000000006,-10" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="Pixel" name="offset_unit" type="QString"/>
            <Option value="0,0,0,0" name="outline_color" type="QString"/>
            <Option value="solid" name="outline_style" type="QString"/>
            <Option value="0" name="outline_width" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
            <Option value="Pixel" name="outline_width_unit" type="QString"/>
            <Option value="diameter" name="scale_method" type="QString"/>
            <Option value="5.4" name="size" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
            <Option value="Pixel" name="size_unit" type="QString"/>
            <Option value="1" name="vertical_anchor_point" type="QString"/>
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
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="if(TO_REAL( &quot;Azimuth&quot; )=0,'',TO_REAL( &quot;Azimuth&quot; ))" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
                <Option name="size" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="if( &quot;AZIMUTH&quot; !=0,5.4,0)" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer locked="0" pass="0" class="SimpleMarker" enabled="1">
          <Option type="Map">
            <Option value="0" name="angle" type="QString"/>
            <Option value="255,255,255,255" name="color" type="QString"/>
            <Option value="1" name="horizontal_anchor_point" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="square" name="name" type="QString"/>
            <Option value="0,0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="Pixel" name="offset_unit" type="QString"/>
            <Option value="97,97,97,255" name="outline_color" type="QString"/>
            <Option value="solid" name="outline_style" type="QString"/>
            <Option value="0" name="outline_width" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
            <Option value="Pixel" name="outline_width_unit" type="QString"/>
            <Option value="diameter" name="scale_method" type="QString"/>
            <Option value="14" name="size" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
            <Option value="Pixel" name="size_unit" type="QString"/>
            <Option value="1" name="vertical_anchor_point" type="QString"/>
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
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option value="false" name="active" type="bool"/>
                  <Option value="if(TO_REAL( &quot;Azimuth&quot; )=0,'',TO_REAL( &quot;Azimuth&quot; ))" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer locked="0" pass="0" class="SimpleMarker" enabled="1">
          <Option type="Map">
            <Option value="0" name="angle" type="QString"/>
            <Option value="97,97,97,255" name="color" type="QString"/>
            <Option value="1" name="horizontal_anchor_point" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="triangle" name="name" type="QString"/>
            <Option value="-2,1" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="Pixel" name="offset_unit" type="QString"/>
            <Option value="0,0,0,0" name="outline_color" type="QString"/>
            <Option value="solid" name="outline_style" type="QString"/>
            <Option value="0" name="outline_width" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
            <Option value="Pixel" name="outline_width_unit" type="QString"/>
            <Option value="diameter" name="scale_method" type="QString"/>
            <Option value="5" name="size" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
            <Option value="Pixel" name="size_unit" type="QString"/>
            <Option value="1" name="vertical_anchor_point" type="QString"/>
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
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option value="false" name="active" type="bool"/>
                  <Option value="if(TO_REAL( &quot;Azimuth&quot; )=0,'',TO_REAL( &quot;Azimuth&quot; ))" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer locked="0" pass="0" class="SimpleMarker" enabled="1">
          <Option type="Map">
            <Option value="0" name="angle" type="QString"/>
            <Option value="97,97,97,255" name="color" type="QString"/>
            <Option value="1" name="horizontal_anchor_point" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="triangle" name="name" type="QString"/>
            <Option value="2,0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="Pixel" name="offset_unit" type="QString"/>
            <Option value="0,0,0,0" name="outline_color" type="QString"/>
            <Option value="solid" name="outline_style" type="QString"/>
            <Option value="0" name="outline_width" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
            <Option value="Pixel" name="outline_width_unit" type="QString"/>
            <Option value="diameter" name="scale_method" type="QString"/>
            <Option value="7" name="size" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
            <Option value="Pixel" name="size_unit" type="QString"/>
            <Option value="1" name="vertical_anchor_point" type="QString"/>
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
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option value="false" name="active" type="bool"/>
                  <Option value="if(TO_REAL( &quot;Azimuth&quot; )=0,'',TO_REAL( &quot;Azimuth&quot; ))" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer locked="0" pass="0" class="SimpleMarker" enabled="1">
          <Option type="Map">
            <Option value="0" name="angle" type="QString"/>
            <Option value="97,97,97,255" name="color" type="QString"/>
            <Option value="1" name="horizontal_anchor_point" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="square" name="name" type="QString"/>
            <Option value="-1,-3" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="Pixel" name="offset_unit" type="QString"/>
            <Option value="0,0,0,0" name="outline_color" type="QString"/>
            <Option value="solid" name="outline_style" type="QString"/>
            <Option value="0" name="outline_width" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
            <Option value="Pixel" name="outline_width_unit" type="QString"/>
            <Option value="diameter" name="scale_method" type="QString"/>
            <Option value="2" name="size" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
            <Option value="Pixel" name="size_unit" type="QString"/>
            <Option value="1" name="vertical_anchor_point" type="QString"/>
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
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option value="false" name="active" type="bool"/>
                  <Option value="if(TO_REAL( &quot;Azimuth&quot; )=0,'',TO_REAL( &quot;Azimuth&quot; ))" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
                <Option name="size" type="Map">
                  <Option value="false" name="active" type="bool"/>
                  <Option value="if( &quot;AZIMUTH&quot; !=0,2,0)" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <customproperties>
    <property key="dualview/previewExpressions" value="&quot;Name&quot;"/>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory height="15" minScaleDenominator="0" labelPlacementMethod="XHeight" enabled="0" spacing="0" showAxis="0" maxScaleDenominator="1e+08" rotationOffset="270" width="15" penWidth="0" backgroundColor="#ffffff" barWidth="5" spacingUnit="MM" backgroundAlpha="255" sizeType="MM" opacity="1" diagramOrientation="Up" lineSizeScale="3x:0,0,0,0,0,0" lineSizeType="MM" spacingUnitScale="3x:0,0,0,0,0,0" penColor="#000000" sizeScale="3x:0,0,0,0,0,0" scaleBasedVisibility="0" penAlpha="255" direction="1" scaleDependency="Area" minimumSize="0">
      <fontProperties description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" style=""/>
      <attribute field="" color="#000000" label=""/>
      <axisSymbol>
        <symbol alpha="1" force_rhr="0" name="" clip_to_extent="1" type="line">
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
          <layer locked="0" pass="0" class="SimpleLine" enabled="1">
            <Option type="Map">
              <Option value="0" name="align_dash_pattern" type="QString"/>
              <Option value="square" name="capstyle" type="QString"/>
              <Option value="5;2" name="customdash" type="QString"/>
              <Option value="3x:0,0,0,0,0,0" name="customdash_map_unit_scale" type="QString"/>
              <Option value="MM" name="customdash_unit" type="QString"/>
              <Option value="0" name="dash_pattern_offset" type="QString"/>
              <Option value="3x:0,0,0,0,0,0" name="dash_pattern_offset_map_unit_scale" type="QString"/>
              <Option value="MM" name="dash_pattern_offset_unit" type="QString"/>
              <Option value="0" name="draw_inside_polygon" type="QString"/>
              <Option value="bevel" name="joinstyle" type="QString"/>
              <Option value="35,35,35,255" name="line_color" type="QString"/>
              <Option value="solid" name="line_style" type="QString"/>
              <Option value="0.26" name="line_width" type="QString"/>
              <Option value="MM" name="line_width_unit" type="QString"/>
              <Option value="0" name="offset" type="QString"/>
              <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
              <Option value="MM" name="offset_unit" type="QString"/>
              <Option value="0" name="ring_filter" type="QString"/>
              <Option value="0" name="tweak_dash_pattern_on_corners" type="QString"/>
              <Option value="0" name="use_custom_dash" type="QString"/>
              <Option value="3x:0,0,0,0,0,0" name="width_map_unit_scale" type="QString"/>
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
                <Option value="" name="name" type="QString"/>
                <Option name="properties"/>
                <Option value="collection" name="type" type="QString"/>
              </Option>
            </data_defined_properties>
          </layer>
        </symbol>
      </axisSymbol>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings priority="0" zIndex="0" obstacle="0" linePlacementFlags="18" showAll="1" placement="0" dist="0">
    <properties>
      <Option type="Map">
        <Option value="" name="name" type="QString"/>
        <Option name="properties"/>
        <Option value="collection" name="type" type="QString"/>
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
    <field configurationFlags="None" name="fid">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="ID">
      <editWidget type="Hidden">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Name">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Date">
      <editWidget type="DateTime">
        <config>
          <Option type="Map">
            <Option value="true" name="allow_null" type="bool"/>
            <Option value="true" name="calendar_popup" type="bool"/>
            <Option value="yyyy-MM-dd" name="display_format" type="QString"/>
            <Option value="yyyy-MM-dd" name="field_format" type="QString"/>
            <Option value="false" name="field_iso_format" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Time">
      <editWidget type="DateTime">
        <config>
          <Option type="Map">
            <Option value="true" name="allow_null" type="bool"/>
            <Option value="true" name="calendar_popup" type="bool"/>
            <Option value="HH:mm:ss" name="display_format" type="QString"/>
            <Option value="HH:mm:ss" name="field_format" type="QString"/>
            <Option value="false" name="field_iso_format" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Lon">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Lat">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Altitude">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="North">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Azimuth">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Camera Maker">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Camera Model">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Title">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Comment">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Path">
      <editWidget type="ExternalResource">
        <config>
          <Option type="Map">
            <Option value="0" name="DocumentViewer" type="int"/>
            <Option value="0" name="DocumentViewerHeight" type="int"/>
            <Option value="0" name="DocumentViewerWidth" type="int"/>
            <Option value="true" name="FileWidget" type="bool"/>
            <Option value="true" name="FileWidgetButton" type="bool"/>
            <Option value="" name="FileWidgetFilter" type="QString"/>
            <Option name="PropertyCollection" type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="propertyRootPath" type="Map">
                  <Option value="false" name="active" type="bool"/>
                  <Option value="" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
            <Option value="1" name="RelativeStorage" type="int"/>
            <Option value="0" name="StorageMode" type="int"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="RelPath">
      <editWidget type="ExternalResource">
        <config>
          <Option type="Map">
            <Option value="0" name="DocumentViewer" type="int"/>
            <Option value="350" name="DocumentViewerHeight" type="int"/>
            <Option value="350" name="DocumentViewerWidth" type="int"/>
            <Option value="true" name="FileWidget" type="bool"/>
            <Option value="true" name="FileWidgetButton" type="bool"/>
            <Option value="" name="FileWidgetFilter" type="QString"/>
            <Option name="PropertyCollection" type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
            <Option value="1" name="RelativeStorage" type="int"/>
            <Option value="0" name="StorageMode" type="int"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Timestamp">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Images">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias field="fid" index="0" name=""/>
    <alias field="ID" index="1" name=""/>
    <alias field="Name" index="2" name=""/>
    <alias field="Date" index="3" name=""/>
    <alias field="Time" index="4" name=""/>
    <alias field="Lon" index="5" name=""/>
    <alias field="Lat" index="6" name=""/>
    <alias field="Altitude" index="7" name=""/>
    <alias field="North" index="8" name=""/>
    <alias field="Azimuth" index="9" name=""/>
    <alias field="Camera Maker" index="10" name=""/>
    <alias field="Camera Model" index="11" name=""/>
    <alias field="Title" index="12" name=""/>
    <alias field="Comment" index="13" name=""/>
    <alias field="Path" index="14" name=""/>
    <alias field="RelPath" index="15" name=""/>
    <alias field="Timestamp" index="16" name=""/>
    <alias field="Images" index="17" name=""/>
  </aliases>
  <defaults>
    <default field="fid" applyOnUpdate="0" expression=""/>
    <default field="ID" applyOnUpdate="0" expression=""/>
    <default field="Name" applyOnUpdate="0" expression=""/>
    <default field="Date" applyOnUpdate="0" expression=""/>
    <default field="Time" applyOnUpdate="0" expression=""/>
    <default field="Lon" applyOnUpdate="0" expression=""/>
    <default field="Lat" applyOnUpdate="0" expression=""/>
    <default field="Altitude" applyOnUpdate="0" expression=""/>
    <default field="North" applyOnUpdate="0" expression=""/>
    <default field="Azimuth" applyOnUpdate="0" expression=""/>
    <default field="Camera Maker" applyOnUpdate="0" expression=""/>
    <default field="Camera Model" applyOnUpdate="0" expression=""/>
    <default field="Title" applyOnUpdate="0" expression=""/>
    <default field="Comment" applyOnUpdate="0" expression=""/>
    <default field="Path" applyOnUpdate="0" expression=""/>
    <default field="RelPath" applyOnUpdate="0" expression=""/>
    <default field="Timestamp" applyOnUpdate="0" expression=""/>
    <default field="Images" applyOnUpdate="0" expression=""/>
  </defaults>
  <constraints>
    <constraint field="fid" unique_strength="1" notnull_strength="1" constraints="3" exp_strength="0"/>
    <constraint field="ID" unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint field="Name" unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint field="Date" unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint field="Time" unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint field="Lon" unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint field="Lat" unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint field="Altitude" unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint field="North" unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint field="Azimuth" unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint field="Camera Maker" unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint field="Camera Model" unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint field="Title" unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint field="Comment" unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint field="Path" unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint field="RelPath" unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint field="Timestamp" unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint field="Images" unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="fid" exp="" desc=""/>
    <constraint field="ID" exp="" desc=""/>
    <constraint field="Name" exp="" desc=""/>
    <constraint field="Date" exp="" desc=""/>
    <constraint field="Time" exp="" desc=""/>
    <constraint field="Lon" exp="" desc=""/>
    <constraint field="Lat" exp="" desc=""/>
    <constraint field="Altitude" exp="" desc=""/>
    <constraint field="North" exp="" desc=""/>
    <constraint field="Azimuth" exp="" desc=""/>
    <constraint field="Camera Maker" exp="" desc=""/>
    <constraint field="Camera Model" exp="" desc=""/>
    <constraint field="Title" exp="" desc=""/>
    <constraint field="Comment" exp="" desc=""/>
    <constraint field="Path" exp="" desc=""/>
    <constraint field="RelPath" exp="" desc=""/>
    <constraint field="Timestamp" exp="" desc=""/>
    <constraint field="Images" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortOrder="1" sortExpression="&quot;Camera Model&quot;">
    <columns>
      <column width="63" name="ID" type="field" hidden="0"/>
      <column width="-1" type="actions" hidden="1"/>
      <column width="-1" name="Name" type="field" hidden="0"/>
      <column width="35" name="Date" type="field" hidden="0"/>
      <column width="-1" name="Time" type="field" hidden="0"/>
      <column width="-1" name="Lon" type="field" hidden="0"/>
      <column width="-1" name="Lat" type="field" hidden="0"/>
      <column width="-1" name="Altitude" type="field" hidden="0"/>
      <column width="35" name="North" type="field" hidden="0"/>
      <column width="35" name="Azimuth" type="field" hidden="0"/>
      <column width="-1" name="Path" type="field" hidden="0"/>
      <column width="-1" name="Title" type="field" hidden="0"/>
      <column width="-1" name="Comment" type="field" hidden="0"/>
      <column width="393" name="RelPath" type="field" hidden="0"/>
      <column width="137" name="Timestamp" type="field" hidden="0"/>
      <column width="452" name="Images" type="field" hidden="0"/>
      <column width="-1" name="fid" type="field" hidden="0"/>
      <column width="-1" name="Camera Maker" type="field" hidden="0"/>
      <column width="-1" name="Camera Model" type="field" hidden="0"/>
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
  <editorlayout>tablayout</editorlayout>
  <attributeEditorForm>
    <attributeEditorField index="1" name="ID" showLabel="1"/>
    <attributeEditorField index="2" name="Name" showLabel="1"/>
    <attributeEditorField index="3" name="Date" showLabel="1"/>
    <attributeEditorField index="4" name="Time" showLabel="1"/>
    <attributeEditorField index="5" name="Lon" showLabel="1"/>
    <attributeEditorField index="6" name="Lat" showLabel="1"/>
    <attributeEditorField index="7" name="Altitude" showLabel="1"/>
    <attributeEditorField index="8" name="North" showLabel="1"/>
    <attributeEditorField index="9" name="Azimuth" showLabel="1"/>
    <attributeEditorField index="-1" name="Camera Mak" showLabel="1"/>
    <attributeEditorField index="-1" name="Camera Mod" showLabel="1"/>
    <attributeEditorField index="12" name="Title" showLabel="1"/>
    <attributeEditorField index="13" name="Comment" showLabel="1"/>
    <attributeEditorField index="14" name="Path" showLabel="1"/>
    <attributeEditorField index="15" name="RelPath" showLabel="1"/>
    <attributeEditorHtmlElement name="PhotoView" showLabel="1">&lt;script>document.write('&lt;img src="' + expression.evaluate("\"Path\"")+'" width="350" height="350">');&lt;/script></attributeEditorHtmlElement>
    <attributeEditorField index="16" name="Timestamp" showLabel="1"/>
    <attributeEditorField index="17" name="Images" showLabel="1"/>
  </attributeEditorForm>
  <editable>
    <field editable="1" name="ALTITUDE"/>
    <field editable="1" name="AZIMUTH"/>
    <field editable="1" name="Altitude"/>
    <field editable="1" name="Azimuth"/>
    <field editable="1" name="CAMERA MAK"/>
    <field editable="1" name="CAMERA MOD"/>
    <field editable="1" name="Camera Mak"/>
    <field editable="1" name="Camera Maker"/>
    <field editable="1" name="Camera Mod"/>
    <field editable="1" name="Camera Model"/>
    <field editable="1" name="Comment"/>
    <field editable="1" name="DATE"/>
    <field editable="1" name="Date"/>
    <field editable="1" name="ID"/>
    <field editable="1" name="Images"/>
    <field editable="1" name="LAT"/>
    <field editable="1" name="LON"/>
    <field editable="1" name="Lat"/>
    <field editable="1" name="Lon"/>
    <field editable="1" name="NAME"/>
    <field editable="1" name="NORTH"/>
    <field editable="1" name="Name"/>
    <field editable="1" name="North"/>
    <field editable="1" name="PATH"/>
    <field editable="1" name="Path"/>
    <field editable="1" name="RelPath"/>
    <field editable="1" name="TIME"/>
    <field editable="1" name="Time"/>
    <field editable="1" name="Timestamp"/>
    <field editable="1" name="Title"/>
    <field editable="1" name="fid"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="ALTITUDE"/>
    <field labelOnTop="0" name="AZIMUTH"/>
    <field labelOnTop="0" name="Altitude"/>
    <field labelOnTop="0" name="Azimuth"/>
    <field labelOnTop="0" name="CAMERA MAK"/>
    <field labelOnTop="0" name="CAMERA MOD"/>
    <field labelOnTop="0" name="Camera Mak"/>
    <field labelOnTop="0" name="Camera Maker"/>
    <field labelOnTop="0" name="Camera Mod"/>
    <field labelOnTop="0" name="Camera Model"/>
    <field labelOnTop="0" name="Comment"/>
    <field labelOnTop="0" name="DATE"/>
    <field labelOnTop="0" name="Date"/>
    <field labelOnTop="0" name="ID"/>
    <field labelOnTop="0" name="Images"/>
    <field labelOnTop="0" name="LAT"/>
    <field labelOnTop="0" name="LON"/>
    <field labelOnTop="0" name="Lat"/>
    <field labelOnTop="0" name="Lon"/>
    <field labelOnTop="0" name="NAME"/>
    <field labelOnTop="0" name="NORTH"/>
    <field labelOnTop="0" name="Name"/>
    <field labelOnTop="0" name="North"/>
    <field labelOnTop="0" name="PATH"/>
    <field labelOnTop="0" name="Path"/>
    <field labelOnTop="0" name="RelPath"/>
    <field labelOnTop="0" name="TIME"/>
    <field labelOnTop="0" name="Time"/>
    <field labelOnTop="0" name="Timestamp"/>
    <field labelOnTop="0" name="Title"/>
    <field labelOnTop="0" name="fid"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>"Name"</previewExpression>
  <mapTip>&lt;img src="file:///[% Path %]" width="350" height="250"></mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>
